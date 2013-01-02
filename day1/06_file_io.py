
def main():
	f = open("thoreau.txt")
	for line in f:
		print line.strip()
	f.close()

	g = open('tmp.txt', 'w') #Use 'w+' to append instead of rewrite
	g.write("output is easy too.\n")
	g.close()

if __name__ == "__main__":
	main()
