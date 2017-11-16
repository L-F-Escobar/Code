/*


 *************************************************************************
 ************ CHAPTER 02 - x86 Processor Architecture *****************
 *************************************************************************
 * Protected mode
 * 	32 bit address (4,294,967,295) 4 GB
 * Real-address & virtual-8086 modes
 * 	20 bit address (1,048,575) 1 MB
 * 	in protected mode running mult. program, each program
 * 	has its own 1 MB memory area
 *
 *	8 bits	(256)
 *
 ****** 32 BIT GENERAL PURPOSE REGISTERS ********
 *
 * 		ex.	[8 bits	| 8 bits]
 * 			[   AH	|	AL  ] - 8 bits
 * 		   *[		AX		] - 16 bits
 * 			[				EAX				] - 32 bits
 * 		   * means that those registers only have a 16 bit name
 * 		     of their lower half ie no seperate 8 bit registers.
 *
 * 		     Without means that those registers have 2 8 bit, 1 16
 * 		     bit & itself a 32 bit register.
 *
 * 	EAX  - Accumulator //Specialized
 * 	EBX
 * 	ECX  - Loop counter//Specialized
 * 	EDX
 * 	*EBP - Extended frame pointer (stack)	-	//Specialized
 * 	*ESP - Stack pointer	 SP				All	//Specialized
 * 	*ESI - Index register	 SI				16	//Specialized
 * 	*EDI - Index register	 DI 			BIT	//Specialized
 *
 * 				16 bit SEGEMENT REGISTERS (s-regs)
 *
 * 	CS - Code segment
 * 	SS - Stack segment
 * 	DS - Data segment
 * 	ES - Additional segment
 * 	FS - Additional segment
 * 	GS - Additional segment
 *
 *
 * 	EFLAGS - Status & control flags.
 * 	         Each flag is a single binary bit (1/0)
 * 	         Flag set when it equals 1, it is clear(reset) when
 * 	         it equals 0
 * 	EIP	   - Instruction pointer : Contains the address of the next
 * 								   instruction to be executed
 *
 * 						State Flags
 *
 * 	Carry	: unsigned arithmetic out of range
 * 	Overflow: signed arithmetic out of range
 * 	Sign	: results in a negative
 * 	Zero	: retult is zero
 * 	Auxiliary Carry : Carry from bit 3 to bit 4
 * 	Parity	: sum of 1 bits is an even number
 *
 * 				Floating point, MMX, XMM Registers
 *
 * Eight 80 bit floating point register
 *
 * 	ST(0), ST(1), ST(2), ST(3), ST(4), ... , ST(7)
 *
 * Eight 64 bit MMX Registers
 *
 * Eight 128 bit XMM registers for single instruction multiple
 * data operations (SIMD)








 *************************************************************************
 *********** CHAPTER 03 - Assembly Lang. Fundementals **************
 *************************************************************************
 *
 * Basic Elements of Assembly Language
 *  Integer constants
 *  Int expressions
 *  Char & string const
 *  Reserved words & identifiers
 *  Directions & instructions
 *  Labels
 *  Mnemonics & operands
 *  Comments
 *
 *  Examples :	main PROC
				mov eax, 5		; move 5 to the EAX register
				add eax, 6 		; add 6 to the EAX register
				call WriteInt 	; display value in EAX
				exit 			; quit
				main ENDP
		Add two numbers and displays the result
 *
 *  h - Hexademical
 *  q | o - Octal
 *  d - Decimal
 *  b - Binary
 *  r - Encoded real
 *  	EX. 30d, 6Ah, 42, 1101b, 0AFh
 *
 *  'A' "A" = 1 byte in ASCII
 *  'ABC' "ABC" = Each char occupie a single bye in ASCII
 *
 * LABELS
 * 	Act as place markers for LOOPS - very important
 * 	EX. 	target: //colon mark
 * 				mov ax, bx
 * 				...
 * 				jump target
 *
 * Mnemonics
 * 	MOV, ADD, SUB, MUL, INC, DEC
 * Operands
 * 	constant	96
 * 	constant expression	2+4
 * 	register	eax
 * 	memory	(data label)	count
 *
 * 	EXAMPLE : 	STC instruction
						stc 			; set Carry flag
				INC instruction
						inc eax 		; add 1 to EAX
				MOV instruction
						mov count, ebx 	; move EBX to count
 	 	 	 	 	 	 	 	 	 	; first operation is destination
										; second is the source
				IMUL instruction (three operands)
						imul eax, ebx, 5; ebx multiplied by 5,
										; product in EAX
 *
 * Comments
 * 	For a brick of comment begin with: ! COMMENTS &
 * 							 end with:   COMMENTS &
 *
 * NOP Instruction
 * 	Takes up one byte and mainly used to align code
 *
 * 	EX. 00000000 66 8B C3  mov ax, bx
		00000003 90 	   nop   		; align next instruction
		00000004 8B D1 	   mov edx, ecx
 *
 * ADDING & SUBTRACTING INTEGERS
 *
  ; AddTwo.asm – adds two 32-bit integers
  .386
  .model flat,stdcall
  .stack 4096
  ExitProcess PROTO, dwExitCode:DWORD
  .code
  main PROC
  	  mov eax,5 	; move 5 to the EAX register
	  add eax,6 	; add 6 to the EAX register
	  INVOKE ExitProcess,0
  main ENDP
  END main
 *
 * REQUIRE CODING STANDARDS
 *  	Program Header
 			;Program Description:
 			;Author:
 			;Creation Date:
 			;Revisions:
			;Date: 				Modified by:
 *
 *
 * Example of assembly code
 *
 * 	; This program adds and subtracts 32-bit integers.
	.386
	.MODEL flat,stdcall
	.STACK 4096

	ExitProcess PROTO, dwExitCode:DWORD
	DumpRegs PROTO

	.code
	main PROC
		mov eax,10000h ; EAX = 10000h
		add eax,40000h ; EAX = 50000h
		sub eax,20000h ; EAX = 30000h
		call DumpRegs
		INVOKE ExitProcess,0
	main ENDP
	END main
 *
 ****************** Program Template ********************
; Program Template (Template.asm)

; Program Description:
; Author:
; Creation Date:
; Revisions:
; Date: 				Modified by:

.386
.model flat,stdcall
.stack 4096

ExitProcess PROTO, dwExitCode:DWORD
.data
	; declare variables here

.code
main PROC
	; write your code here
	INVOKE ExitProcess,0
main ENDP
	; (insert additional procedures here)
END main
 *
 *
 * Defining Data
 * 	Byte	: 1(8 bit unsigned/signed integer)//2 binary
 * 	WORD	: 15(16 bit unsigned/signed integer)
 * 	DWORD	: 31(32 bit unsigned/signed integer)
 * 	QWORD	: 63(64 bit integer)
 * 	TBYTE	: 79(80 bit integer)
 *
 * Intrinsic Data types
 *  REAL4 	(4 byte IEEE short real)
 *  REAL8	(8 byte IEEE LONG REAL )
 *  REAL10	(10 byte IEEE extended real)
 *


 ****** DEFINGING DATA VERY IMPORTING SECTION INC ****
 *
 *
 *
 *
 * 	DEFINING BYTE Data

	BYTE 8 bit storage //2^8
	signed   -128 - -1			//smallest -
					 0 - 127	//			 largest
	unsigned         0  -  255 	//smallest to largest

   .data
  		[name]       [init]
  		numOne	BYTE 10		; All initializers become binary
  							;  data in memory
  		value1 	BYTE 'A' 	; character constant
		value2 	BYTE 0 		; smallest unsigned byte
		value3 	BYTE 255 	; largest unsigned byte
		value4 	SBYTE -128  ; smallest signed byte
		value5 	SBYTE +127  ; largest signed byte
		value6 	BYTE ? 		; uninitialized byte


 *
 *
 *
 *	DEFINING WORD and SWORD Data

	WORD & SWORD 16 bit storage // 2^16
	signed    -32768 - -1			//smallest -
					    0 - 32767	//			 largest
	unsigned            0     -      65536	//smallest - largest

	.data

		word1  WORD  65535 		; largest unsigned value
		word2  SWORD –32768 	; smallest signed value
		word3  WORD  ? 			; uninitialized, unsigned
		word4  WORD  "AB" 		; double characters
		myList WORD  1,2,3,4,5 	; array of words
		array  WORD  5 DUP(?) 	; uninitialized array


 *
 *
 *
 *	DEFINING DWORD and SDWORD Data

 	DWORD & SDWORD 32 bit storage //2^32
 	signed	-2,147,483,648 - -1
 							  0 - -2,147,483,647
 	unsigned 0 - 4,294,967,295

 	.data

		val1 DWORD 	12345678h 	 ; unsigned
		val2 SDWORD –2147483648  ; signed
		val3 DWORD 	20 DUP(?) 	 ; unsigned array
		val4 SDWORD –3,–2,–1,0,1 ; signed array

 *
 *
 *
 * DEFINGING QWORD, TBYTE & Real Data

   .data

   quad1  QWORD 1234567812345678h
	val1  TBYTE 1000000000123456789Ah
	rVal1 REAL4 -2.1
	rVal2 REAL8 3.2E-260
	rVal3 REAL10 4.6E+4096
	ShortArray REAL4 20 DUP(0.0)




 *** DEFINING STRINGS *** - (null-terminated ends with ,0)
 *
 * 		str1 	 BYTE "Enter your name",0
		str2 	 BYTE 'Error: halting program',0
		str3 	 BYTE 'A','E','I','O','U'
		greeting BYTE "Welcome to the Encryption Demo program "
 	 	 	 	 BYTE "created by Kip Irvine.",0
 *
 *
 * To continue a single string across multiple
   lines, end each line with a comma:

	menu BYTE "Checking Account",0dh,0ah,0dh,0ah,
		"1. Create a new account",0dh,0ah,
		"2. Open an existing account",0dh,0ah,
		"3. Credit the account",0dh,0ah,
		"4. Debit the account",0dh,0ah,
		"5. Exit",0ah,0

	– 0dh = carriage return
	– 0ah = line feed
	- newLine BYTE 0Dh,0Ah,0


 * DUP Operator - very important
 *
 * var1 BYTE 20 DUP(0) 		; 20 bytes, all equal to zero
   var2 BYTE 20 DUP(?) 		; 20 bytes, uninitialized
   var3 BYTE 4 DUP("STACK") ; 20 bytes: "STACKSTACKSTACKSTACK"
   var4 BYTE 10,3 DUP(0),20 ; 5 bytes
   	   	   	   	   	   	    ; var4 [10], [0], [0], [0], [20]
 *
 *
 *
 *
 * Little Endian Order
  	All data types larger then a byte store their individual
  	bytes in reverse  order.

  	EX. val1 DWORD 12345678h	0000[78]
  								0001[56]
  								0002[34]
  								0003[12]

  *
  *
  *
  *
  * TITLE Add and Subtract, Version 2 (AddSub2.asm)
	; This program adds and subtracts 32-bit unsigned
	; integers and stores the sum in a variable.

	INCLUDE Irvine32.inc
	.data
		val1 DWORD 10000h
		val2 DWORD 40000h
		val3 DWORD 20000h
		finalVal DWORD ?

	.code
	main PROC
		mov  eax,val1 	  ; start with 10000h
		add  eax,val2 	  ; add 40000h
		sub  eax,val3 	  ; subtract 20000h
		mov  finalVal,eax ; store the result (30000h)
		call DumpRegs 	  ; display the registers
		exit
	main ENDP
	END main


 *
 *
 *
 * Symbolic constants
 	 EX. COUNT = 500
 	 	 .
 	 	 .
 	 	 move ax,COUNT


 *
 *
 *
 * CALC size of a BYTE array
 	current location counter: $
 	-subtract address of list
 	-difference is the number of bytes

 		ex. list BYTE 10, 20, 30, 40
 		    ListSize = ($ - list)

 *
 *
 *
 * CALC size of a WORD array
 	Divide total number of bytes by 2(the size of a word)

 		ex. list WORD 1000h, 2000h, 3000h, 4000h
 			ListSize = ($ - list) / 2


 *
 *
 *
 * CALC the size of a DWORD array
 	Divide total number of bytes by 4(the size of a dword)

 		ex. list DWORD 1, 2, 3, 4
 			ListSize = ($ - list) / 4


 *
 *
 *
 * EQU Directive //Same As
    Define a symbol as either an integer or text expression
    Cannot be redefined

    	ex. PI EQU <3.1416>
    		pressKey EQU <"Press any key to continue..",0>
    		.data
    		prompt BYTE pressKey


 *
 *
 *
 * TEXTEQU Directive
    Defines a symbol as either an int or text expression
    Called a text macro
    Can be redefined

    	ex. continueMsg TEXTEQU <"Do you wish to continue (Y/N)?">
		 	rowSize = 5
			.data
			prompt1 BYTE continueMsg
			count TEXTEQU %(rowSize * 2) ; evaluates the expression
			setupAL TEXTEQU <mov al,count>
			.code
			setupAL ; generates: "mov al,10"



 * Use	64-bit	registers	when	possible
*/







