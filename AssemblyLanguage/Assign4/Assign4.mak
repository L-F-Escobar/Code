ALL: Assign4.EXE 

CLEAN: 
 -@erase Assign4.EXE 
 -@erase Assign4.ILK 
 -@erase Assign4.PDB 
 -@erase Assign4.OBJ 
 -@erase Assign4.LST 

Assign4.ASM: 

Assign4.OBJ: Assign4.ASM 
 ml /c /coff /Zi Assign4.ASM 

Assign4.EXE: Assign4.OBJ 
 link /debug /subsystem:console /out:Assign4.EXE /entry:start Assign4.OBJ KERNEL32.LIB IO.OBJ

