        .ORIG x3000
        LD R1, DATA
        LD R2, A
        NOT R3, R1
        ADD R3, R3, #-15 ;取R1相反数减16
first   LDR R5, R1, #0
        STR R5, R2, #0
        ADD R1, R1, #1
        ADD R2, R2, #1
        ADD R4, R1, R3
        BRn first ;循环结束时实现把x4000——x400D中的数据全部按照原样搬进x5000及后续地址中
        LD R1, A
        ADD R1, R1, #-1
        ADD R0, R0, #-1
Second  ADD R1, R1, #1
        LD R7, A
        NOT R7, R7
        ADD R7, R7, #-14
        ADD R6, R1, R7
        ADD R6, R6, #-1
        BRp Third
        ADD R0, R0, #1
        ADD R7, R7, R0
        LD R2, A
Four    LDR R3, R2, #0
        LDR R4, R2, #1
        ADD R2, R2, #1
        ADD R6, R2, R7
        BRp Second
        NOT R5, R3
        ADD R5, R5, #1
        ADD R5, R5, R4
        BRzp Four
        STR R3, R2, #0
        STR R4, R2, #-1
        BRnzp Four
Third   AND R1, R1, #0
        AND R2, R2, #0
        AND R7, R7, #0
        LD R4, D
        NOT R4, R4
        ADD R4, R4, #1
        LD R0, E
        NOT R0, R0
        ADD R0, R0, #1
        ADD R1, R1, #4
        ADD R2, R2, #8
        LD R3, B
        ADD R3, R3, #1
seven   ADD R1, R1, #0
        BRz five
        ADD R3, R3, #-1
        LDR R5, R3, #0
        ADD R1, R1, #-1
        ADD R2, R2, #-1
        ADD R6, R5, R4
        BRzp six
        BRn thirt
eight   AND R7, R7, #0
        ADD R1, R1, #0
        BRp twelve
eleven  ADD R2, R2, #0
        BRz nine
        ADD R3, R3, #-1
        LDR R5, R3, #0
        ADD R2, R2, #-1
        ADD R6, R5, R0
        BRzp ten
        BRn nine
        
        
        
DATA    .Fill x4000
A       .Fill x5000
B       .Fill x500f
C       .Fill x5100
F       .Fill x5008
D       .Fill x55
E       .Fill x4B
G       .Fill x5101
six     ADD R7, R7, #1
        BRp seven
ten     ADD R7, R7, #1
        BRp eleven
five    LD R6, C
        STR R7, R6, #0
        ADD R7, R7, #0
        BRzp eight
thirt   LD R6, C
        ADD R3, R3, #1
        STR R7, R6, #0
        ADD R7, R7, #0
        BRzp eight
twelve  ADD R2, R2, #1
        BRp eleven
nine    LD R4, G
        STR R7, R4, #0
        .END
        TRAP x25