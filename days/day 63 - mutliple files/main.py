import subroutines as sub
import time

sub.colourChange("r")

list_2D = [[1,2,3],[4,5,6],[7,8,9]]
sub.print2DArray(list_2D)

dict_2D = {"a":{"b":1,"c":2},"d":{"e":3,"f":4}}
sub.printDict2D(dict_2D)


print("Clearing screen in: ")
sub.countdown()
print("Clearing screen now")
time.sleep(0.5)
sub.clear()
