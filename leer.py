
def run():
    counter = 0
    with open("aleph.txt") as f:
        for line in f:
            counter += line.count("Beatriz")
    print("Beatriz se encuentra {} veces en el etexto".format(counter))

if __name__=='__main__':
    run()
