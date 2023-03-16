kata = (2019, 9, 25, 3, 30)
#MM/DD/YYYY MM:SS
if __name__ == "__main__":
	month = str(kata[1])
	day = str(kata[2])
	year = str(kata[0])
	hour = str(kata[3])
	minute = str(kata[4])
	print(f'{month.zfill(2)}/{day.zfill(2)}/{year.zfill(4)} {hour.zfill(2)}:{minute.zfill(2)}')