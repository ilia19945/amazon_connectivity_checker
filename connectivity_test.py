import time
import grequests
import csv

time.asctime()

try:
    f = open(f"connectivity_test_results [{time.tzname[0]}], {time.strftime('%m-%d-%Y',time.localtime(time.time()))}.csv", "a+", newline='')
    writer = csv.DictWriter(
        f, fieldnames=["datetime", "instanceNW", "instanceFF", "instanceLND", "time_taken", f"time_start = {time.strftime('%H:%M:%S',time.localtime(time.time()))}"])
    writer.writeheader()
    f.close()
except Exception as e:
    print("Couldn't append results. Error: ", e)
    pass

urls = [
    'https://ieluqbvv.telemetry.connect.us-east-1.amazonaws.com/ping',
    'https://ieluqbvv.telemetry.connect.eu-central-1.amazonaws.com/ping',
    'https://ieluqbvv.telemetry.connect.eu-west-2.amazonaws.com/ping',
]

rounds = 0


def exception_handler(request, exception):
    return request.url


while True:
    result = []
    t0 = time.time()
    if rounds % 2 == 0:
        for iteration in range(10):
            rs = (grequests.get(url, timeout=10) for url in urls)
            responses = grequests.map(rs, exception_handler=exception_handler)

            if iteration == 0:
                for i in responses:
                    try:
                        result.append([i.elapsed.total_seconds(), i.url])
                    except Exception as e:
                        result.append(["couldn't ping", urls[responses.index(i)]])
            else:
                for i in range(len(result)):
                    # print(result[i][0])
                    try:
                        if type(result[i][0]) is str:
                            result[i] = ["couldn't ping", urls[responses.index(responses[i])]]

                        else:
                            if result[i][0] > responses[i].elapsed.total_seconds():
                                result[i][0] = responses[i].elapsed.total_seconds()
                            else:
                                pass
                    except Exception as e:
                        result[i] = [f"couldn't ping", urls[responses.index(responses[i])]]

        t1 = time.time()
        time_taken = round(t1 - t0, 4)
        print(f'Checking at: {time.strftime("%H:%M:%S",time.localtime(t0))} (10 attempts). Time taken: {time_taken}')
        row = [time.strftime("%H:%M:%S", time.localtime(t0))]
        for res in range(len(result)):
            row.append(str(result[res][0]))
        row.append(time_taken)
        try:
            file = open(f"connectivity_test_results [{time.tzname[0]}], {time.strftime('%m-%d-%Y',time.localtime(time.time()))}.csv", "a+", newline='')
            writer = csv.writer(file)
            writer.writerow(row)
            file.close()
        except Exception as e:
            print("Couldn't append results. Error: ", e)
            pass
    else:
        print(f'Sleeping until: {time.strftime("%H:%M:%S", time.localtime(time.time() + 60))}')
        time.sleep(60)

    rounds += 1
