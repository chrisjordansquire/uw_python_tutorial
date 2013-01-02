import re
import collections


def main():
	#I'm using the with keywork to avoid having to call f.close()
	#once I'm done with the file f
	with open('thoreau.txt') as f:

		text = [line for line in f] #a file object is iterable
		text = None

		#The above can be bad because it reads the entire file in at once.
		#We can also process it line by line using a for loop, since files
		#are iterable
		word_counts = collections.defaultdict(int)
		f.seek(0)
		word_re = re.compile('[A-Za-z]+')

		for line in f:
			line = line.strip().lower()
			words = word_re.findall(line)
			for word in words:
				word_counts[word] += 1

	sorted_word_counts = sorted(word_counts.items(),
			key=lambda x:x[1], reverse=True)

	with open('thoreau_counts.txt', 'w') as g:
		for word, count in sorted_word_counts:
			g.write(word + " : " + str(count) + "\n")


if __name__ == "__main__":
	main()

