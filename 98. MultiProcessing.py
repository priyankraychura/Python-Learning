import multiprocessing
import requests
import concurrent.futures

def downloadFile(url, name):
    print(f"Started downloading {name}")
    response = requests.get(url)
    open(f"./files/file{name}.jpg", "wb").write(response.content)
    print(f"Finished downloading {name}")

url = "https://picsum.photos/2000/3000"

def main():
    if __name__ == '__main__':
        pros = []
        for i in range(5):
            # downloadFile(url, i)
            p = multiprocessing.Process(target=downloadFile, args=[url, i])
            p.start()
            pros.append(p)

        for p in pros:
            p.join()

def poolingDemo():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(5)]
        l2 = [i for i in range(5)]
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)

if __name__ == '__main__':
    poolingDemo()