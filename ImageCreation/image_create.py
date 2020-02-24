import numpy as np
import cv2

#red 0,0,255
def main():
	parkingLot = np.zeros((512,512,3),np.uint8) #all black screen
	parkingLot = cv2.rectangle(parkingLot, (75,85), (105,115), (0,255,0),3) #12
	parkingLot = cv2.rectangle(parkingLot, (115,85), (145,115), (0,255,0),3) #13
	parkingLot = cv2.rectangle(parkingLot, (337,85), (367,115), (0,255,0),3) #18
	parkingLot = cv2.rectangle(parkingLot, (377,85), (407,115), (0,255,0),3) #19


	parkingLot = cv2.rectangle(parkingLot, (25,185), (55,215), (0,0,255),3) #3
	parkingLot = cv2.rectangle(parkingLot, (25,225), (55,255), (0,255,0),3) #2
	parkingLot = cv2.rectangle(parkingLot, (25,265), (55,295), (0,255,0),3) #1
	parkingLot = cv2.rectangle(parkingLot, (25,305), (55,335), (0,255,0),3) #0

	parkingLot = cv2.rectangle(parkingLot, (195,185), (225,215), (0,255,0),3) #4
	parkingLot = cv2.rectangle(parkingLot, (195,225), (225,255), (0,255,0),3) #5
	parkingLot = cv2.rectangle(parkingLot, (195,265), (225,295), (0,255,0),3) #6
	parkingLot = cv2.rectangle(parkingLot, (195,305), (225,335), (0,255,0),3) #7

	parkingLot = cv2.rectangle(parkingLot, (287,185), (317,215), (0,255,0),3) #8
	parkingLot = cv2.rectangle(parkingLot, (287,225), (317,255), (0,255,0),3) #9
	parkingLot = cv2.rectangle(parkingLot, (287,265), (317,295), (0,255,0),3) #10
	parkingLot = cv2.rectangle(parkingLot, (287,305), (317,335), (0,255,0),3) #11

	parkingLot = cv2.rectangle(parkingLot, (457,185), (487,215), (0,255,0),3) #14
	parkingLot = cv2.rectangle(parkingLot, (457,225), (487,255), (0,255,0),3) #15
	parkingLot = cv2.rectangle(parkingLot, (457,265), (487,295), (0,255,0),3) #16
	parkingLot = cv2.rectangle(parkingLot, (457,305), (487,335), (0,255,0),3) #17

	parkingLot = cv2.rectangle(parkingLot, (95,400), (125,430), (255,0,0),3) #23
	parkingLot = cv2.rectangle(parkingLot, (357,400), (387,430), (255,0,0),3) #22

	cv2.imshow("parkingLot", parkingLot)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()