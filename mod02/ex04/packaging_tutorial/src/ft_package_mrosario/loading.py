import time
import datetime

def ft_progress(lst: list):
	start_time = datetime.datetime.now()
	ms_time_diff = 0
	total_elems = len(lst)
	remaining_elems = 0
	width = 20
	fill_width = 0
	fill_bar = str()
	for elem in lst:
		ms_time_diff = (datetime.datetime.now() - start_time).total_seconds() * 1000
		remaining_elems = total_elems - lst.index(elem)
		processed_elems = total_elems - remaining_elems
		percentage_remaining = 100 * remaining_elems / total_elems
		percentage_complete = 100 - percentage_remaining
		mean_delta_time = ms_time_diff / (1 if processed_elems == 0 else processed_elems)
		remaining_time = mean_delta_time * remaining_elems * 0.001
		fill_width = 0 if percentage_complete == 0 else width - (width * percentage_remaining * 0.01)
		fill_bar = str().ljust(int(fill_width), '=') + '>'
		progress_bar = str(f"\rETA: {(remaining_time):.1f}s [{percentage_complete:6.2f}%] [{str(fill_bar).ljust(width, ' ')}] {processed_elems}/{total_elems} | elapsed time: {ms_time_diff * 0.001:.2f}s")
		progress_bar_len = len(progress_bar)
		print(progress_bar, end="")
		yield elem
		print(str('\r').ljust(progress_bar_len), end="")
	print(f"\rETA: 0s [100%] [{str(fill_bar).ljust(width, ' ')}] {total_elems}/{total_elems} | elapsed time: {ms_time_diff * 0.001:.2f}", end="")

def main():
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy): # esto significa while((elem = elem->next))
		ret += (elem + 3) % 5
		time.sleep(0.01)
	print()
	print(ret)

if __name__ == "__main__":
	main()
