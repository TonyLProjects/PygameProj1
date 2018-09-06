# TODO: check out python unit test

from inputBuffer import inputBuffer 
import inputStruct

myBuffer = inputBuffer(sizeLimit = 5)
myBuffer.printBuffer()
print("initial buffer size", myBuffer.getBufferSize())

for i in range(5):
	myBuffer.enqueue(i)
print("insert 0~4 to buffer.size is now: ", myBuffer.getBufferSize())
myBuffer.printBuffer()

print("deque 1 element")
myBuffer.dequeue()
myBuffer.printBuffer()

print("clearing buffer")
myBuffer.clearBuffer()
myBuffer.printBuffer()
for i in range(5):
	myBuffer.enqueue(i)
print("insert 0~4 to buffer.size is now: ", myBuffer.getBufferSize())
myBuffer.printBuffer()
print("buffer size: ", myBuffer.getBufferSize())

print("adding element in full buffer")
myBuffer.enqueue(9)
myBuffer.printBuffer()
print("buffer size: ", myBuffer.getBufferSize())

print("clearing buffer")
myBuffer.clearBuffer()
print("dequeue from empty buffer")
myBuffer.dequeue()