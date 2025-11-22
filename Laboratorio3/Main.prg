Global Integer i
Global Integer posA(30)
Global Integer posB(30)
Function main
	Motor On
	Power High
	Accel 100, 100
	Speed 100
	Home
	Do
		On Out_9
		Call Paletizado_01
		On Out_9
		Home
	Loop

	
Fend
Function Paletizado_01

    Pallet 1, origen, puntox, puntoy, 6, 5
    
    '--Posiciones A
    posA(0) = 1
	posA(1) = 14
	posA(2) = 25
	posA(3) = 21
	posA(4) = 29
	posA(5) = 18
	posA(6) = 5
	posA(7) = 9
	posA(8) = 13
	posA(9) = 26
	posA(10) = 22
	posA(11) = 30
	posA(12) = 17
	posA(13) = 6
	posA(14) = 10
	posA(15) = 2
	posA(16) = 15
	posA(17) = 19
	posA(18) = 27
	posA(19) = 23
	posA(20) = 12
	posA(21) = 4
	posA(22) = 8
	posA(23) = 16
	posA(24) = 24
	posA(25) = 11
	posA(26) = 3
	posA(27) = 7
	posA(28) = 20
	posA(29) = 28
	posA(30) = 1
	'--Posiciones B
	posB(0) = 30
	posB(1) = 17
	posB(2) = 6
	posB(3) = 10
	posB(4) = 2
	posB(5) = 13
	posB(6) = 25
	posB(7) = 22
	posB(8) = 18
	posB(9) = 5
	posB(10) = 9
	posB(11) = 1
	posB(12) = 14
	posB(13) = 25
	posB(14) = 21
	posB(15) = 29
	posB(16) = 16
	posB(17) = 12
	posB(18) = 4
	posB(19) = 8
	posB(20) = 19
	posB(21) = 27
	posB(22) = 23
	posB(23) = 15
	posB(24) = 7
	posB(25) = 20
	posB(26) = 28
	posB(27) = 24
	posB(28) = 11
	posB(29) = 3
	posB(30) = 30
	For i = 0 To 29
		
			Jump Pallet(1, posA(i))
		   	Off Out_9
		   	Wait 0.5
		    Jump Pallet(1, posA(i + 1))
		   	On Out_9
			Jump Pallet(1, posB(i))
		   	Off Out_9
		   	Wait 0.5
		    Jump Pallet(1, posB(i + 1))
		   	On Out_9
		   	Print "Movimiento ", i + 1

	Next

Fend
Function prueba
		Pallet 1, origen, puntox, puntoy, 6, 5
		For i = 1 To 30
		    Jump Pallet(1, i)
		Next
Fend
Function ventosa
	Off Out_9
	Wait 5
	On Out_9
Fend

