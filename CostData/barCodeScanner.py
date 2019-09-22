import win32com.client 
import pythoncom
import time

class EvHandler:
	def OnBarCodeIn(self,_1):
		print(_1)

scanner = win32com.client.DispatchWithEvents("BarcodeScanner.Reader", EvHandler)
scanner.Visible=True

while 1:
	pythoncom.PumpWaitingMessages()
	time.sleep(0.8)