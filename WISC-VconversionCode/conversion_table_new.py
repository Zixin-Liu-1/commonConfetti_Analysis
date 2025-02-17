# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:55:52 2025

@author: Liu
"""
conversion_tables = {
    
    
    
    # These tables are for 4. Zahlen Nachsprechen Task
    #
    
    
    (7, 2, 4): {
        **{i: 1 for i in range(0, 6)},       # 0-5 -> 1
        **{i: 2 for i in range(6, 7)},       # 6 -> 2
        **{i: 3 for i in range(7, 9)},       # 7-8 -> 3
        **{i: 4 for i in range(9, 11)},      # 9-10 -> 4
        **{i: 5 for i in range(11, 13)},     # 11-12 -> 5
        **{i: 6 for i in range(13, 15)},     # 13-14 -> 6
        **{i: 7 for i in range(15, 16)},     # 15 -> 7
        **{i: 8 for i in range(16, 18)},     # 16-17 -> 8
        **{i: 9 for i in range(18, 20)},     # 18-19 -> 9
        **{i: 10 for i in range(20, 21)},    # 20 -> 10
        **{i: 11 for i in range(21, 23)},    # 21-22 -> 11
        **{i: 12 for i in range(23, 25)},    # 23-24 -> 12
        **{i: 13 for i in range(25, 26)},    # 25 -> 13
        **{i: 14 for i in range(26, 28)},    # 26-27 -> 14
        **{i: 15 for i in range(28, 29)},    # 28 -> 15
        **{i: 16 for i in range(29, 31)},    # 29-30 -> 16
        **{i: 17 for i in range(31, 33)},    # 31-32 -> 17
        **{i: 18 for i in range(33, 34)},    # 33 -> 18
        **{i: 19 for i in range(34, 55)}     # 34-54 -> 19
    },
    
    (8, 0, 4): {
        **{i: 1 for i in range(0, 7)},      # 0-6 -> 1
        **{i: 2 for i in range(7, 8)},      # 7 -> 2
        **{i: 3 for i in range(8, 10)},     # 8-9 -> 3
        **{i: 4 for i in range(10, 12)},    # 10-11 -> 4
        **{i: 5 for i in range(12, 14)},    # 12-13 -> 5
        **{i: 6 for i in range(14, 15)},    # 14 -> 6
        **{i: 7 for i in range(15, 17)},    # 15-16 -> 7
        **{i: 8 for i in range(17, 19)},    # 17-18 -> 8
        **{i: 9 for i in range(19, 20)},    # 19 -> 9
        **{i: 10 for i in range(20, 22)},   # 20-21 -> 10
        **{i: 11 for i in range(22, 24)},   # 22-23 -> 11
        **{i: 12 for i in range(24, 25)},   # 24 -> 12
        **{i: 13 for i in range(25, 27)},   # 25-26 -> 13
        **{i: 14 for i in range(27, 29)},   # 27-28 -> 14
        **{i: 15 for i in range(29, 30)},   # 29 -> 15
        **{i: 16 for i in range(30, 32)},   # 30-31 -> 16
        **{i: 17 for i in range(32, 34)},   # 32-33 -> 17
        **{i: 18 for i in range(34, 35)},   # 34 -> 18
        **{i: 19 for i in range(35, 55)}    # 35-54 -> 19
    },
    
    (8, 1, 4): {
        **{i: 1 for i in range(0, 7)},      # 0-6 -> 1
        **{i: 2 for i in range(7, 9)},      # 7-8 -> 2
        **{i: 3 for i in range(9, 11)},     # 9-10 -> 3
        **{i: 4 for i in range(11, 13)},    # 11-12 -> 4
        **{i: 5 for i in range(13, 14)},    # 13 -> 5
        **{i: 6 for i in range(14, 16)},    # 14-15 -> 6
        **{i: 7 for i in range(16, 18)},    # 16-17 -> 7
        **{i: 8 for i in range(18, 19)},    # 18 -> 8
        **{i: 9 for i in range(19, 21)},    # 19-20 -> 9
        **{i: 10 for i in range(21, 23)},   # 21-22 -> 10
        **{i: 11 for i in range(23, 25)},   # 23-24 -> 11
        **{i: 12 for i in range(24, 25)},   # 24 -> 12
        **{i: 13 for i in range(25, 27)},   # 25-26 -> 13
        **{i: 14 for i in range(27, 29)},   # 27-28 -> 14
        **{i: 15 for i in range(29, 30)},   # 29 -> 15
        **{i: 16 for i in range(30, 32)},   # 30-31 -> 16
        **{i: 17 for i in range(32, 34)},   # 32-33 -> 17
        **{i: 18 for i in range(34, 36)},   # 34-35 -> 18
        **{i: 19 for i in range(36, 55)}    # 36-54 -> 19
    },
    
    (8, 2, 4): {
        **{i: 1 for i in range(0, 7)},      # 0-6 -> 1
        **{i: 2 for i in range(7, 9)},      # 7-8 -> 2
        **{i: 3 for i in range(9, 11)},     # 9-10 -> 3
        **{i: 4 for i in range(11, 13)},    # 11-12 -> 4
        **{i: 5 for i in range(13, 15)},    # 13-14 -> 5
        **{i: 6 for i in range(15, 17)},    # 15-16 -> 6
        **{i: 7 for i in range(16, 18)},    # 16-17 -> 7
        **{i: 8 for i in range(18, 20)},    # 18-19 -> 8
        **{i: 9 for i in range(19, 21)},    # 19-20 -> 9
        **{i: 10 for i in range(21, 24)},   # 21-23 -> 10
        **{i: 11 for i in range(24, 25)},   # 24 -> 11
        **{i: 12 for i in range(25, 27)},   # 25-26 -> 12
        **{i: 13 for i in range(27, 29)},   # 27-28 -> 13
        **{i: 14 for i in range(29, 30)},   # 29 -> 14
        **{i: 15 for i in range(30, 32)},   # 30-31 -> 15
        **{i: 16 for i in range(32, 34)},   # 32-33 -> 16
        **{i: 17 for i in range(34, 35)},   # 34 -> 17
        **{i: 18 for i in range(35, 37)},   # 35-36 -> 18
        **{i: 19 for i in range(37, 55)}    # 37-54 -> 19
    },
    
    (9, 0, 4): {
        **{i: 1 for i in range(0, 7)},      # 0-6 -> 1
        **{i: 2 for i in range(7, 9)},      # 7-8 -> 2
        **{i: 3 for i in range(9, 11)},     # 9-10 -> 3
        **{i: 4 for i in range(11, 13)},    # 11-12 -> 4
        **{i: 5 for i in range(14, 15)},    # 14 -> 5
        **{i: 6 for i in range(15, 17)},    # 15-16 -> 6
        **{i: 7 for i in range(17, 19)},    # 17-18 -> 7
        **{i: 8 for i in range(19, 21)},    # 19-20 -> 8
        **{i: 9 for i in range(21, 22)},    # 21 -> 9
        **{i: 10 for i in range(22, 24)},   # 22-23 -> 10
        **{i: 11 for i in range(24, 26)},   # 24-25 -> 11
        **{i: 12 for i in range(26, 27)},   # 26 -> 12
        **{i: 13 for i in range(27, 29)},   # 27-28 -> 13
        **{i: 14 for i in range(29, 31)},   # 29-30 -> 14
        **{i: 15 for i in range(31, 33)},   # 31-32 -> 15
        **{i: 16 for i in range(33, 35)},   # 33-34 -> 16
        **{i: 17 for i in range(34, 36)},   # 34-35 -> 17
        **{i: 18 for i in range(35, 37)},   # 35-36 -> 18
        **{i: 19 for i in range(37, 55)}    # 37-54 -> 19
    },
    
   
    
    (9, 1, 4): {
        **{i: 1 for i in range(0, 9)},      # 0-8 -> 1
        **{i: 2 for i in range(9, 11)},     # 9-10 -> 2
        **{i: 3 for i in range(11, 12)},    # 11 -> 3
        **{i: 4 for i in range(12, 14)},    # 12-13 -> 4
        **{i: 5 for i in range(14, 16)},    # 14-15 -> 5
        **{i: 6 for i in range(16, 18)},    # 16-17 -> 6
        **{i: 7 for i in range(17, 19)},    # 17-18 -> 7
        **{i: 8 for i in range(19, 21)},    # 19-20 -> 8
        **{i: 9 for i in range(21, 23)},    # 21-22 -> 9
        **{i: 10 for i in range(23, 25)},   # 23-24 -> 10
        **{i: 11 for i in range(25, 26)},   # 25 -> 11
        **{i: 12 for i in range(26, 28)},   # 26-27 -> 12
        **{i: 13 for i in range(28, 30)},   # 28-29 -> 13
        **{i: 14 for i in range(29, 31)},   # 29-30 -> 14
        **{i: 15 for i in range(31, 33)},   # 31-32 -> 15
        **{i: 16 for i in range(33, 35)},   # 33-34 -> 16
        **{i: 17 for i in range(34, 36)},   # 34-35 -> 17
        **{i: 18 for i in range(35, 38)},   # 35-37 -> 18
        **{i: 19 for i in range(38, 55)}    # 38-54 -> 19
    },
    
    (9, 2, 4): {
        **{i: 1 for i in range(0, 9)},      # 0-8 -> 1
        **{i: 2 for i in range(9, 11)},     # 9-10 -> 2
        **{i: 3 for i in range(11, 13)},    # 11-12 -> 3
        **{i: 4 for i in range(12, 14)},    # 12-13 -> 4
        **{i: 5 for i in range(14, 16)},    # 14-15 -> 5
        **{i: 6 for i in range(16, 18)},    # 16-17 -> 6
        **{i: 7 for i in range(17, 19)},    # 17-18 -> 7
        **{i: 8 for i in range(19, 21)},    # 19-20 -> 8
        **{i: 9 for i in range(21, 23)},    # 21-22 -> 9
        **{i: 10 for i in range(23, 25)},   # 23-24 -> 10
        **{i: 11 for i in range(25, 27)},   # 25-26 -> 11
        **{i: 12 for i in range(27, 28)},   # 27 -> 12
        **{i: 13 for i in range(28, 30)},   # 28-29 -> 13
        **{i: 14 for i in range(29, 31)},   # 29-30 -> 14
        **{i: 15 for i in range(31, 33)},   # 31-32 -> 15
        **{i: 16 for i in range(33, 35)},   # 33-34 -> 16
        **{i: 17 for i in range(34, 36)},   # 34-35 -> 17
        **{i: 18 for i in range(35, 40)},   # 35-39 -> 18
        **{i: 19 for i in range(40, 55)}    # 40-54 -> 19
    },
    
    (10, 0, 4): {
        **{i: 1 for i in range(0, 10)},     # 0-9 -> 1
        **{i: 2 for i in range(10, 11)},    # 10 -> 2
        **{i: 3 for i in range(11, 13)},    # 11-12 -> 3
        **{i: 4 for i in range(13, 15)},    # 13-14 -> 4
        **{i: 5 for i in range(14, 17)},    # 14-16 -> 5
        **{i: 6 for i in range(17, 18)},    # 17 -> 6
        **{i: 7 for i in range(18, 20)},    # 18-19 -> 7
        **{i: 8 for i in range(20, 22)},    # 20-21 -> 8
        **{i: 9 for i in range(22, 24)},    # 22-23 -> 9
        **{i: 10 for i in range(24, 25)},   # 24 -> 10
        **{i: 11 for i in range(25, 27)},   # 25-26 -> 11
        **{i: 12 for i in range(27, 29)},   # 27-28 -> 12
        **{i: 13 for i in range(29, 31)},   # 29-30 -> 13
        **{i: 14 for i in range(31, 32)},   # 31 -> 14
        **{i: 15 for i in range(32, 34)},   # 32-33 -> 15
        **{i: 16 for i in range(34, 36)},   # 34-35 -> 16
        **{i: 17 for i in range(36, 37)},   # 36 -> 17
        **{i: 18 for i in range(37, 39)},   # 37-38 -> 18
        **{i: 19 for i in range(39, 55)}    # 39-54 -> 19
    },
    
    (10, 1, 4): {
        **{i: 1 for i in range(0, 10)},      # 0-9 -> 1
        **{i: 2 for i in range(10, 12)},     # 10-11 -> 2
        **{i: 3 for i in range(12, 13)},     # 12 -> 3
        **{i: 4 for i in range(13, 15)},     # 13-14 -> 4
        **{i: 5 for i in range(15, 17)},     # 15-16 -> 5
        **{i: 6 for i in range(17, 19)},     # 17-18 -> 6
        **{i: 7 for i in range(19, 20)},     # 19 -> 7
        **{i: 8 for i in range(20, 22)},     # 20-21 -> 8
        **{i: 9 for i in range(22, 24)},     # 22-23 -> 9
        **{i: 10 for i in range(24, 26)},    # 24-25 -> 10
        **{i: 11 for i in range(26, 27)},    # 26 -> 11
        **{i: 12 for i in range(27, 29)},    # 27-28 -> 12
        **{i: 13 for i in range(29, 31)},    # 29-30 -> 13
        **{i: 14 for i in range(31, 33)},    # 31-32 -> 14
        **{i: 15 for i in range(33, 34)},    # 33 -> 15
        **{i: 16 for i in range(34, 36)},    # 34-35 -> 16
        **{i: 17 for i in range(36, 38)},    # 36-37 -> 17
        **{i: 18 for i in range(38, 40)},    # 38-39 -> 18
        **{i: 19 for i in range(40, 55)}     # 40-54 -> 19
    },
    
    (10, 2, 4): {
        **{i: 1 for i in range(0, 10)},      # 0-9 -> 1
        **{i: 2 for i in range(10, 12)},     # 10-11 -> 2
        **{i: 3 for i in range(12, 14)},     # 12-13 -> 3
        **{i: 4 for i in range(14, 16)},     # 14-15 -> 4
        **{i: 5 for i in range(15, 17)},     # 15-16 -> 5
        **{i: 6 for i in range(17, 19)},     # 17-18 -> 6
        **{i: 7 for i in range(19, 21)},     # 19-20 -> 7
        **{i: 8 for i in range(21, 23)},     # 21-22 -> 8
        **{i: 9 for i in range(22, 24)},     # 22-23 -> 9
        **{i: 10 for i in range(24, 26)},    # 24-25 -> 10
        **{i: 11 for i in range(26, 28)},    # 26-27 -> 11
        **{i: 12 for i in range(28, 29)},    # 28 -> 12
        **{i: 13 for i in range(29, 31)},    # 29-30 -> 13
        **{i: 14 for i in range(31, 33)},    # 31-32 -> 14
        **{i: 15 for i in range(33, 35)},    # 33-34 -> 15
        **{i: 16 for i in range(35, 36)},    # 35 -> 16
        **{i: 17 for i in range(36, 38)},    # 36-37 -> 17
        **{i: 18 for i in range(38, 40)},    # 38-39 -> 18
        **{i: 19 for i in range(40, 55)}     # 40-54 -> 19
    },
    
    (11, 0, 4): {
        **{i: 1 for i in range(0, 10)},      # 0-9 -> 1
        **{i: 2 for i in range(10, 12)},     # 10-11 -> 2
        **{i: 3 for i in range(12, 14)},     # 12-13 -> 3
        **{i: 4 for i in range(14, 16)},     # 14-15 -> 4
        **{i: 4 for i in range(15, 16)},     # 15 -> 4
        **{i: 5 for i in range(15, 17)},     # 15-16 -> 5
        **{i: 6 for i in range(17, 19)},     # 17-18 -> 6
        **{i: 7 for i in range(19, 21)},     # 19-20 -> 7
        **{i: 8 for i in range(21, 23)},     # 21-22 -> 8
        **{i: 9 for i in range(23, 24)},     # 23 -> 9
        **{i: 10 for i in range(24, 26)},    # 24-25 -> 10
        **{i: 11 for i in range(26, 28)},    # 26-27 -> 11
        **{i: 12 for i in range(28, 30)},    # 28-29 -> 12
        **{i: 13 for i in range(30, 31)},    # 30 -> 13
        **{i: 14 for i in range(31, 33)},    # 31-32 -> 14
        **{i: 15 for i in range(33, 35)},    # 33-34 -> 15
        **{i: 16 for i in range(35, 37)},    # 35-36 -> 16
        **{i: 17 for i in range(37, 39)},    # 37-38 -> 17
        **{i: 18 for i in range(39, 40)},    # 39 -> 18
        **{i: 19 for i in range(40, 55)}     # 40-54 -> 19
    },
    
    
    # These tables are for 5. Zahlen Symbol Test Task
    #
    (7, 2, 5): {
        **{i: 1 for i in range(0, 13)},    # 0-12 -> 1
        **{i: 2 for i in range(13, 15)},   # 13-14 -> 2
        **{i: 3 for i in range(15, 17)},   # 15-16 -> 3
        **{i: 4 for i in range(17, 19)},   # 17-18 -> 4
        **{i: 5 for i in range(19, 22)},   # 19-21 -> 5
        **{i: 6 for i in range(22, 24)},   # 22-23 -> 6
        **{i: 7 for i in range(24, 27)},   # 24-26 -> 7
        **{i: 8 for i in range(27, 31)},   # 27-30 -> 8
        **{i: 9 for i in range(31, 35)},   # 31-34 -> 9
        **{i: 10 for i in range(35, 39)},  # 35-38 -> 10
        **{i: 11 for i in range(39, 43)},  # 39-42 -> 11
        **{i: 12 for i in range(43, 47)},  # 43-46 -> 12
        **{i: 13 for i in range(47, 51)},  # 47-50 -> 13
        **{i: 14 for i in range(51, 56)},  # 51-55 -> 14
        **{i: 15 for i in range(56, 60)},  # 56-59 -> 15
        **{i: 16 for i in range(60, 65)},  # 60-64 -> 16
        **{i: 17 for i in range(65, 69)},  # 65-68 -> 17
        **{i: 18 for i in range(69, 73)},  # 69-72 -> 18
        **{i: 19 for i in range(73, 75)},  # 73-75 -> 19
    },
    
    (8, 0, 5): {
        **{i: 1 for i in range(0, 12)},    # 0-11 -> 1
        **{i: 2 for i in range(12, 13)},   # 12 -> 2
        **{i: 3 for i in range(13, 15)},   # 13-14 -> 3
        **{i: 4 for i in range(15, 17)},   # 15-16 -> 4
        **{i: 5 for i in range(17, 19)},   # 17-18 -> 5
        **{i: 6 for i in range(19, 21)},   # 19-20 -> 6
        **{i: 7 for i in range(21, 23)},   # 21-22 -> 7
        **{i: 8 for i in range(23, 26)},   # 23-25 -> 8
        **{i: 9 for i in range(26, 29)},   # 26-28 -> 9
        **{i: 10 for i in range(29, 32)},  # 29-31 -> 10
        **{i: 11 for i in range(32, 35)},  # 32-34 -> 11
        **{i: 12 for i in range(35, 38)},  # 35-37 -> 12
        **{i: 13 for i in range(38, 42)},  # 38-41 -> 13
        **{i: 14 for i in range(42, 45)},  # 42-44 -> 14
        **{i: 15 for i in range(45, 49)},  # 45-48 -> 15
        **{i: 16 for i in range(49, 53)},  # 49-52 -> 16
        **{i: 17 for i in range(53, 57)},  # 53-56 -> 17
        **{i: 18 for i in range(57, 61)},  # 57-60 -> 18
        **{i: 19 for i in range(61, 117)},  # 61-117 -> 19
    },
    
    (8, 1, 5): {
        **{i: 1 for i in range(0, 13)},      # 0-12 -> 1
        **{i: 2 for i in range(13, 14)},     # 13 -> 2
        **{i: 3 for i in range(14, 16)},     # 14-15 -> 3
        **{i: 4 for i in range(16, 18)},     # 16-17 -> 4
        **{i: 5 for i in range(18, 20)},     # 18-19 -> 5
        **{i: 6 for i in range(20, 22)},     # 20-21 -> 6
        **{i: 7 for i in range(22, 25)},     # 22-24 -> 7
        **{i: 8 for i in range(25, 27)},     # 25-26 -> 8
        **{i: 9 for i in range(27, 30)},     # 27-29 -> 9
        **{i: 10 for i in range(30, 34)},    # 30-33 -> 10
        **{i: 11 for i in range(34, 37)},    # 34-36 -> 11
        **{i: 12 for i in range(37, 41)},    # 37-40 -> 12
        **{i: 13 for i in range(41, 44)},    # 41-43 -> 13
        **{i: 14 for i in range(44, 48)},    # 44-47 -> 14
        **{i: 15 for i in range(48, 51)},    # 48-50 -> 15
        **{i: 16 for i in range(51, 55)},    # 51-54 -> 16
        **{i: 17 for i in range(55, 60)},    # 55-59 -> 17
        **{i: 18 for i in range(60, 64)},    # 60-63 -> 18
        **{i: 19 for i in range(64, 118)},   # 64-117 -> 19
    },
    
    (8, 2, 5): {
        **{i: 1 for i in range(0, 14)},      # 0-13 -> 1
        **{i: 2 for i in range(14, 15)},     # 14 -> 2
        **{i: 3 for i in range(15, 17)},     # 15-16 -> 3
        **{i: 4 for i in range(17, 19)},     # 17-18 -> 4
        **{i: 5 for i in range(19, 21)},     # 19-20 -> 5
        **{i: 6 for i in range(21, 23)},     # 21-22 -> 6
        **{i: 7 for i in range(23, 26)},     # 23-25 -> 7
        **{i: 8 for i in range(26, 29)},     # 26-28 -> 8
        **{i: 9 for i in range(29, 32)},     # 29-31 -> 9
        **{i: 10 for i in range(32, 35)},    # 32-34 -> 10
        **{i: 11 for i in range(35, 39)},    # 35-38 -> 11
        **{i: 12 for i in range(39, 43)},    # 39-42 -> 12
        **{i: 13 for i in range(43, 46)},    # 43-45 -> 13
        **{i: 14 for i in range(46, 50)},    # 46-49 -> 14
        **{i: 15 for i in range(50, 54)},    # 50-53 -> 15
        **{i: 16 for i in range(54, 58)},    # 54-57 -> 16
        **{i: 17 for i in range(58, 63)},    # 58-62 -> 17
        **{i: 18 for i in range(63, 67)},    # 63-66 -> 18
        **{i: 19 for i in range(67, 118)},   # 67-117 -> 19
    },
    
    (9, 0, 5): {
        **{i: 1 for i in range(0, 14)},      # 0-13 -> 1
        **{i: 2 for i in range(14, 15)},     # 14 -> 2
        **{i: 3 for i in range(15, 17)},     # 15-16 -> 3
        **{i: 4 for i in range(17, 19)},     # 17-18 -> 4
        **{i: 5 for i in range(19, 21)},     # 19-20 -> 5
        **{i: 6 for i in range(21, 24)},     # 21-23 -> 6
        **{i: 7 for i in range(24, 27)},     # 24-26 -> 7
        **{i: 8 for i in range(27, 30)},     # 27-29 -> 8
        **{i: 9 for i in range(30, 33)},     # 30-32 -> 9
        **{i: 10 for i in range(33, 36)},    # 33-35 -> 10
        **{i: 11 for i in range(36, 40)},    # 36-39 -> 11
        **{i: 12 for i in range(40, 44)},    # 40-43 -> 12
        **{i: 13 for i in range(44, 48)},    # 44-47 -> 13
        **{i: 14 for i in range(48, 52)},    # 48-51 -> 14
        **{i: 15 for i in range(52, 56)},    # 52-55 -> 15
        **{i: 16 for i in range(56, 60)},    # 56-59 -> 16
        **{i: 17 for i in range(60, 65)},    # 60-64 -> 17
        **{i: 18 for i in range(65, 70)},    # 65-69 -> 18
        **{i: 19 for i in range(70, 118)},   # 70-117 -> 19
    },
    
    (9, 1, 5): {
        **{i: 1 for i in range(0, 15)},     # 0-14 -> 1
        **{i: 2 for i in range(15, 16)},    # 15 -> 2
        **{i: 3 for i in range(16, 18)},    # 16-17 -> 3
        **{i: 4 for i in range(18, 20)},    # 18-19 -> 4
        **{i: 5 for i in range(20, 23)},    # 20-22 -> 5
        **{i: 6 for i in range(23, 25)},    # 23-24 -> 6
        **{i: 7 for i in range(25, 28)},    # 25-27 -> 7
        **{i: 8 for i in range(28, 31)},    # 28-30 -> 8
        **{i: 9 for i in range(31, 35)},    # 31-34 -> 9
        **{i: 10 for i in range(35, 38)},   # 35-37 -> 10
        **{i: 11 for i in range(38, 42)},   # 38-41 -> 11
        **{i: 12 for i in range(42, 46)},   # 42-45 -> 12
        **{i: 13 for i in range(46, 50)},   # 46-49 -> 13
        **{i: 14 for i in range(50, 54)},   # 50-53 -> 14
        **{i: 15 for i in range(54, 59)},   # 54-58 -> 15
        **{i: 16 for i in range(59, 63)},   # 59-62 -> 16
        **{i: 17 for i in range(63, 68)},   # 63-67 -> 17
        **{i: 18 for i in range(68, 73)},   # 68-72 -> 18
        **{i: 19 for i in range(73, 118)},  # 73-117 -> 19
    },
    
    (9, 2, 5): {
        **{i: 1 for i in range(0, 15)},     # 0-14 -> 1
        **{i: 2 for i in range(15, 17)},    # 15-16 -> 2
        **{i: 3 for i in range(17, 19)},    # 17-18 -> 3
        **{i: 4 for i in range(19, 22)},    # 19-21 -> 4
        **{i: 5 for i in range(22, 24)},    # 22-23 -> 5
        **{i: 6 for i in range(24, 27)},    # 24-26 -> 6
        **{i: 7 for i in range(27, 30)},    # 27-29 -> 7
        **{i: 8 for i in range(30, 33)},    # 30-32 -> 8
        **{i: 9 for i in range(33, 37)},    # 33-36 -> 9
        **{i: 10 for i in range(37, 40)},   # 37-39 -> 10
        **{i: 11 for i in range(40, 44)},   # 40-43 -> 11
        **{i: 12 for i in range(44, 48)},   # 44-47 -> 12
        **{i: 13 for i in range(48, 53)},   # 48-52 -> 13
        **{i: 14 for i in range(53, 57)},   # 53-56 -> 14
        **{i: 15 for i in range(57, 61)},   # 57-60 -> 15
        **{i: 16 for i in range(61, 66)},   # 61-65 -> 16
        **{i: 17 for i in range(66, 71)},   # 66-70 -> 17
        **{i: 18 for i in range(71, 76)},   # 71-75 -> 18
        **{i: 19 for i in range(76, 118)},  # 76-117 -> 19
    },
   
    (10, 0, 5): {
        **{i: 1 for i in range(0, 15)},     # 0-14 -> 1
        **{i: 2 for i in range(15, 18)},    # 15-17 -> 2
        **{i: 3 for i in range(18, 20)},    # 18-19 -> 3
        **{i: 4 for i in range(20, 23)},    # 20-22 -> 4
        **{i: 5 for i in range(23, 26)},    # 23-25 -> 5
        **{i: 6 for i in range(26, 29)},    # 26-28 -> 6
        **{i: 7 for i in range(29, 32)},    # 29-31 -> 7
        **{i: 8 for i in range(32, 35)},    # 32-34 -> 8
        **{i: 9 for i in range(35, 39)},    # 35-38 -> 9
        **{i: 10 for i in range(39, 42)},   # 39-41 -> 10
        **{i: 11 for i in range(42, 46)},   # 42-45 -> 11
        **{i: 12 for i in range(46, 51)},   # 46-50 -> 12
        **{i: 13 for i in range(51, 55)},   # 51-54 -> 13
        **{i: 14 for i in range(55, 60)},   # 55-59 -> 14
        **{i: 15 for i in range(60, 65)},   # 60-64 -> 15
        **{i: 16 for i in range(65, 69)},   # 65-68 -> 16
        **{i: 17 for i in range(69, 74)},   # 69-73 -> 17
        **{i: 18 for i in range(74, 78)},   # 74-77 -> 18
        **{i: 19 for i in range(78, 118)},  # 78-117 -> 19
    },
    
    (10, 1, 5):  {
        **{i: 1 for i in range(0, 16)},     # 0-15 -> 1
        **{i: 2 for i in range(16, 19)},    # 16-18 -> 2
        **{i: 3 for i in range(19, 21)},    # 19-20 -> 3
        **{i: 4 for i in range(21, 24)},    # 21-23 -> 4
        **{i: 5 for i in range(24, 27)},    # 24-26 -> 5
        **{i: 6 for i in range(27, 30)},    # 27-29 -> 6
        **{i: 7 for i in range(30, 34)},    # 30-33 -> 7
        **{i: 8 for i in range(34, 38)},    # 34-37 -> 8
        **{i: 9 for i in range(38, 42)},    # 38-41 -> 9
        **{i: 10 for i in range(42, 45)},   # 42-44 -> 10
        **{i: 11 for i in range(45, 49)},   # 45-48 -> 11
        **{i: 12 for i in range(49, 54)},   # 49-53 -> 12
        **{i: 13 for i in range(54, 58)},   # 54-57 -> 13
        **{i: 14 for i in range(56, 63)},   # 56-62 -> 14
        **{i: 15 for i in range(63, 67)},   # 63-66 -> 15
        **{i: 16 for i in range(67, 72)},   # 67-71 -> 16
        **{i: 17 for i in range(72, 76)},   # 72-75 -> 17
        **{i: 18 for i in range(76, 80)},   # 76-79 -> 18
        **{i: 19 for i in range(80, 118)},  # 80-117 -> 19
    },

    (10, 2, 5): {
        **{i: 1 for i in range(0, 16)},     # 0-15 -> 1
        **{i: 2 for i in range(16, 19)},    # 16-18 -> 2
        **{i: 3 for i in range(19, 22)},    # 19-21 -> 3
        **{i: 4 for i in range(22, 25)},    # 22-24 -> 4
        **{i: 5 for i in range(25, 28)},    # 25-27 -> 5
        **{i: 6 for i in range(28, 32)},    # 28-31 -> 6
        **{i: 7 for i in range(32, 35)},    # 32-34 -> 7
        **{i: 8 for i in range(35, 39)},    # 35-38 -> 8
        **{i: 9 for i in range(39, 43)},    # 39-42 -> 9
        **{i: 10 for i in range(43, 47)},   # 43-46 -> 10
        **{i: 11 for i in range(47, 51)},   # 47-50 -> 11
        **{i: 12 for i in range(51, 55)},   # 51-54 -> 12
        **{i: 13 for i in range(55, 60)},   # 55-59 -> 13
        **{i: 14 for i in range(60, 64)},   # 60-63 -> 14
        **{i: 15 for i in range(64, 69)},   # 64-68 -> 15
        **{i: 16 for i in range(69, 74)},   # 69-73 -> 16
        **{i: 17 for i in range(74, 79)},   # 74-78 -> 17
        **{i: 18 for i in range(79, 83)},   # 79-82 -> 18
        **{i: 19 for i in range(83, 118)},  # 83-117 -> 19
    },
   
    (11, 0, 5): {
        **{i: 1 for i in range(0, 16)},      # 0-15 -> 1
        **{i: 2 for i in range(16, 19)},     # 16-18 -> 2
        **{i: 3 for i in range(19, 22)},     # 19-21 -> 3
        **{i: 4 for i in range(22, 25)},     # 22-24 -> 4
        **{i: 5 for i in range(25, 28)},     # 25-27 -> 5
        **{i: 6 for i in range(28, 32)},     # 28-31 -> 6
        **{i: 7 for i in range(32, 36)},     # 32-35 -> 7
        **{i: 8 for i in range(36, 39)},     # 36-38 -> 8
        **{i: 9 for i in range(39, 43)},     # 39-42 -> 9
        **{i: 10 for i in range(43, 48)},    # 43-47 -> 10
        **{i: 11 for i in range(48, 52)},    # 48-51 -> 11
        **{i: 12 for i in range(52, 56)},    # 52-55 -> 12
        **{i: 13 for i in range(56, 61)},    # 56-60 -> 13
        **{i: 14 for i in range(61, 65)},    # 61-64 -> 14
        **{i: 15 for i in range(65, 70)},    # 65-69 -> 15
        **{i: 16 for i in range(70, 75)},    # 70-74 -> 16
        **{i: 17 for i in range(75, 79)},    # 75-78 -> 17
        **{i: 18 for i in range(79, 83)},    # 79-82 -> 18
        **{i: 19 for i in range(83, 118)},   # 83-117 -> 19
    },
    
    
    # These tables are for 9. Bilderfolgen Task
    #
    
    (7, 2, 9): {
         **{i: 1 for i in range(0, 5)},      # 0-4 -> 1
         **{i: 2 for i in range(5, 7)},      # 5-6 -> 2
         **{i: 3 for i in range(7, 9)},      # 7-8 -> 3
         **{i: 4 for i in range(9, 10)},     # 9-9 -> 4
         **{i: 5 for i in range(10, 12)},    # 10-11 -> 5
         **{i: 6 for i in range(12, 14)},    # 12-13 -> 6
         **{i: 7 for i in range(14, 17)},    # 14-16 -> 7
         **{i: 8 for i in range(17, 19)},    # 17-18 -> 8
         **{i: 9 for i in range(19, 21)},    # 19-20 -> 9
         **{i: 10 for i in range(21, 23)},   # 21-22 -> 10
         **{i: 11 for i in range(23, 26)},   # 23-25 -> 11
         **{i: 12 for i in range(26, 28)},   # 26-27 -> 12
         **{i: 13 for i in range(28, 30)},   # 28-29 -> 13
         **{i: 14 for i in range(30, 33)},   # 30-32 -> 14
         **{i: 15 for i in range(33, 35)},   # 33-34 -> 15
         **{i: 16 for i in range(35, 38)},   # 35-37 -> 16
         **{i: 17 for i in range(38, 40)},   # 38-39 -> 17
         **{i: 18 for i in range(40, 43)},   # 40-42 -> 18
         **{i: 19 for i in range(43, 50)},   # 43-49 -> 19
    },
    
    (8, 0, 9): {
         **{i: 1 for i in range(0, 6)},      # 0-5 -> 1
         **{i: 2 for i in range(6, 7)},      # 6-6 -> 2
         **{i: 3 for i in range(7, 9)},      # 7-8 -> 3
         **{i: 4 for i in range(9, 11)},     # 9-10 -> 4
         **{i: 5 for i in range(11, 13)},    # 11-12 -> 5
         **{i: 6 for i in range(13, 15)},    # 13-14 -> 6
         **{i: 7 for i in range(15, 17)},    # 15-16 -> 7
         **{i: 8 for i in range(17, 19)},    # 17-18 -> 8
         **{i: 9 for i in range(19, 22)},    # 19-21 -> 9
         **{i: 10 for i in range(22, 24)},   # 22-23 -> 10
         **{i: 11 for i in range(24, 26)},   # 24-25 -> 11
         **{i: 12 for i in range(26, 29)},   # 26-28 -> 12
         **{i: 13 for i in range(29, 31)},   # 29-30 -> 13
         **{i: 14 for i in range(31, 33)},   # 31-32 -> 14
         **{i: 15 for i in range(33, 36)},   # 33-35 -> 15
         **{i: 16 for i in range(36, 38)},   # 36-37 -> 16
         **{i: 17 for i in range(38, 41)},   # 38-40 -> 17
         **{i: 18 for i in range(41, 43)},   # 41-42 -> 18
         **{i: 19 for i in range(43, 50)},   # 43-49 -> 19
    },
    
    (8, 1, 9): {
         **{i: 1 for i in range(0, 6)},      # 0-5 -> 1
         **{i: 2 for i in range(6, 8)},      # 6-7 -> 2
         **{i: 3 for i in range(8, 10)},     # 8-9 -> 3
         **{i: 4 for i in range(10, 12)},    # 10-11 -> 4
         **{i: 5 for i in range(12, 14)},    # 12-13 -> 5
         **{i: 6 for i in range(14, 16)},    # 14-15 -> 6
         **{i: 7 for i in range(16, 18)},    # 16-17 -> 7
         **{i: 8 for i in range(18, 20)},    # 18-19 -> 8
         **{i: 9 for i in range(20, 22)},    # 20-21 -> 9
         **{i: 10 for i in range(22, 25)},   # 22-24 -> 10
         **{i: 11 for i in range(25, 27)},   # 25-26 -> 11
         **{i: 12 for i in range(27, 29)},   # 27-28 -> 12
         **{i: 13 for i in range(29, 32)},   # 29-31 -> 13
         **{i: 14 for i in range(32, 34)},   # 32-33 -> 14
         **{i: 15 for i in range(34, 37)},   # 34-36 -> 15
         **{i: 16 for i in range(37, 39)},   # 37-38 -> 16
         **{i: 17 for i in range(39, 41)},   # 39-40 -> 17
         **{i: 18 for i in range(41, 44)},   # 41-43 -> 18
         **{i: 19 for i in range(44, 50)},   # 44-49 -> 19
    },
    
    (8, 2, 9): {
         **{i: 1 for i in range(0, 6)},      # 0-5 -> 1
         **{i: 2 for i in range(6, 8)},      # 6-7 -> 2
         **{i: 3 for i in range(8, 10)},     # 8-9 -> 3
         **{i: 4 for i in range(10, 12)},    # 10-11 -> 4
         **{i: 5 for i in range(12, 14)},    # 12-13 -> 5
         **{i: 6 for i in range(14, 16)},    # 14-15 -> 6
         **{i: 7 for i in range(16, 19)},    # 16-18 -> 7
         **{i: 8 for i in range(19, 21)},    # 19-20 -> 8
         **{i: 9 for i in range(21, 23)},    # 21-22 -> 9
         **{i: 10 for i in range(23, 25)},   # 23-24 -> 10
         **{i: 11 for i in range(25, 28)},   # 25-27 -> 11
         **{i: 12 for i in range(28, 30)},   # 28-29 -> 12
         **{i: 13 for i in range(30, 32)},   # 30-31 -> 13
         **{i: 14 for i in range(32, 35)},   # 32-34 -> 14
         **{i: 15 for i in range(35, 37)},   # 35-36 -> 15
         **{i: 16 for i in range(37, 39)},   # 37-38 -> 16
         **{i: 17 for i in range(39, 42)},   # 39-41 -> 17
         **{i: 18 for i in range(42, 44)},   # 42-43 -> 18
         **{i: 19 for i in range(44, 50)},   # 44-49 -> 19
    },
    
    (9, 0, 9): {
         **{i: 1 for i in range(0, 7)},      # 0-6 -> 1
         **{i: 2 for i in range(7, 9)},      # 7-8 -> 2
         **{i: 3 for i in range(9, 11)},     # 9-10 -> 3
         **{i: 4 for i in range(11, 13)},    # 11-12 -> 4
         **{i: 5 for i in range(13, 15)},    # 13-14 -> 5
         **{i: 6 for i in range(15, 17)},    # 15-16 -> 6
         **{i: 7 for i in range(17, 19)},    # 17-18 -> 7
         **{i: 8 for i in range(19, 21)},    # 19-20 -> 8
         **{i: 9 for i in range(21, 24)},    # 21-23 -> 9
         **{i: 10 for i in range(24, 26)},   # 24-25 -> 10
         **{i: 11 for i in range(26, 28)},   # 26-27 -> 11
         **{i: 12 for i in range(28, 30)},   # 28-29 -> 12
         **{i: 13 for i in range(30, 33)},   # 30-32 -> 13
         **{i: 14 for i in range(33, 35)},   # 33-34 -> 14
         **{i: 15 for i in range(35, 38)},   # 35-37 -> 15
         **{i: 16 for i in range(38, 40)},   # 38-39 -> 16
         **{i: 17 for i in range(40, 42)},   # 40-41 -> 17
         **{i: 18 for i in range(42, 45)},   # 42-44 -> 18
         **{i: 19 for i in range(45, 50)},   # 45-49 -> 19
    },
    
    (9, 1, 9): {
         **{i: 1 for i in range(0, 7)},      # 0-6 -> 1
         **{i: 2 for i in range(7, 9)},      # 7-8 -> 2
         **{i: 3 for i in range(9, 11)},     # 9-10 -> 3
         **{i: 4 for i in range(11, 13)},    # 11-12 -> 4
         **{i: 5 for i in range(13, 15)},    # 13-14 -> 5
         **{i: 6 for i in range(15, 17)},    # 15-16 -> 6
         **{i: 7 for i in range(17, 20)},    # 17-19 -> 7
         **{i: 8 for i in range(20, 22)},    # 20-21 -> 8
         **{i: 9 for i in range(22, 24)},    # 22-23 -> 9
         **{i: 10 for i in range(24, 26)},   # 24-25 -> 10
         **{i: 11 for i in range(26, 29)},   # 26-28 -> 11
         **{i: 12 for i in range(29, 31)},   # 29-30 -> 12
         **{i: 13 for i in range(31, 33)},   # 31-32 -> 13
         **{i: 14 for i in range(33, 36)},   # 33-35 -> 14
         **{i: 15 for i in range(36, 38)},   # 36-37 -> 15
         **{i: 16 for i in range(38, 40)},   # 38-39 -> 16
         **{i: 17 for i in range(40, 43)},   # 40-42 -> 17
         **{i: 18 for i in range(43, 45)},   # 43-44 -> 18
         **{i: 19 for i in range(45, 50)},   # 45-49 -> 19
    },
    
    (9, 2, 9): {
         **{i: 1 for i in range(0, 7)},      # 0-6 -> 1
         **{i: 2 for i in range(7, 9)},      # 7-8 -> 2
         **{i: 3 for i in range(9, 11)},     # 9-10 -> 3
         **{i: 4 for i in range(11, 13)},    # 11-12 -> 4
         **{i: 5 for i in range(13, 16)},    # 13-15 -> 5
         **{i: 6 for i in range(16, 18)},    # 16-17 -> 6
         **{i: 7 for i in range(18, 20)},    # 18-19 -> 7
         **{i: 8 for i in range(20, 22)},    # 20-21 -> 8
         **{i: 9 for i in range(22, 25)},    # 22-24 -> 9
         **{i: 10 for i in range(25, 27)},   # 25-26 -> 10
         **{i: 11 for i in range(27, 29)},   # 27-28 -> 11
         **{i: 12 for i in range(29, 31)},   # 29-30 -> 12
         **{i: 13 for i in range(31, 34)},   # 31-33 -> 13
         **{i: 14 for i in range(34, 36)},   # 34-35 -> 14
         **{i: 15 for i in range(36, 38)},   # 36-37 -> 15
         **{i: 16 for i in range(38, 41)},   # 38-40 -> 16
         **{i: 17 for i in range(41, 43)},   # 41-42 -> 17
         **{i: 18 for i in range(43, 45)},   # 43-44 -> 18
         **{i: 19 for i in range(45, 50)},   # 45-49 -> 19
    },
    
    (10, 0, 9): {
         **{i: 1 for i in range(0, 7)},      # 0-6 -> 1
         **{i: 2 for i in range(7, 9)},      # 7-8 -> 2
         **{i: 3 for i in range(9, 12)},     # 9-11 -> 3
         **{i: 4 for i in range(12, 14)},    # 12-13 -> 4
         **{i: 5 for i in range(14, 16)},    # 14-15 -> 5
         **{i: 6 for i in range(16, 18)},    # 16-17 -> 6
         **{i: 7 for i in range(18, 21)},    # 18-20 -> 7
         **{i: 8 for i in range(21, 23)},    # 21-22 -> 8
         **{i: 9 for i in range(23, 25)},    # 23-24 -> 9
         **{i: 10 for i in range(25, 27)},   # 25-26 -> 10
         **{i: 11 for i in range(27, 30)},   # 27-29 -> 11
         **{i: 12 for i in range(30, 32)},   # 30-31 -> 12
         **{i: 13 for i in range(32, 34)},   # 32-33 -> 13
         **{i: 14 for i in range(34, 37)},   # 34-36 -> 14
         **{i: 15 for i in range(37, 39)},   # 37-38 -> 15
         **{i: 16 for i in range(39, 41)},   # 39-40 -> 16
         **{i: 17 for i in range(41, 43)},   # 41-42 -> 17
         **{i: 18 for i in range(43, 46)},   # 43-45 -> 18
         **{i: 19 for i in range(46, 50)},   # 46-49 -> 19
    },
    
    (10, 1, 9): {
         **{i: 1 for i in range(0, 8)},      # 0-7 -> 1
         **{i: 2 for i in range(8, 10)},     # 8-9 -> 2
         **{i: 3 for i in range(10, 12)},    # 10-11 -> 3
         **{i: 4 for i in range(12, 14)},    # 12-13 -> 4
         **{i: 5 for i in range(14, 16)},    # 14-15 -> 5
         **{i: 6 for i in range(16, 19)},    # 16-18 -> 6
         **{i: 7 for i in range(19, 21)},    # 19-20 -> 7
         **{i: 8 for i in range(21, 23)},    # 21-22 -> 8
         **{i: 9 for i in range(23, 26)},    # 23-25 -> 9
         **{i: 10 for i in range(26, 28)},   # 26-27 -> 10
         **{i: 11 for i in range(28, 30)},   # 28-29 -> 11
         **{i: 12 for i in range(30, 32)},   # 30-31 -> 12
         **{i: 13 for i in range(32, 35)},   # 32-34 -> 13
         **{i: 14 for i in range(35, 37)},   # 35-36 -> 14
         **{i: 15 for i in range(37, 39)},   # 37-38 -> 15
         **{i: 16 for i in range(39, 41)},   # 39-40 -> 16
         **{i: 17 for i in range(41, 44)},   # 41-43 -> 17
         **{i: 18 for i in range(44, 46)},   # 44-45 -> 18
         **{i: 19 for i in range(46, 50)},   # 46-49 -> 19
    },
    
    (10, 2, 9): {
         **{i: 1 for i in range(0, 8)},      # 0-7 -> 1
         **{i: 2 for i in range(8, 10)},     # 8-9 -> 2
         **{i: 3 for i in range(10, 12)},    # 10-11 -> 3
         **{i: 4 for i in range(12, 14)},    # 12-13 -> 4
         **{i: 5 for i in range(14, 17)},    # 14-16 -> 5
         **{i: 6 for i in range(17, 19)},    # 17-18 -> 6
         **{i: 7 for i in range(19, 21)},    # 19-20 -> 7
         **{i: 8 for i in range(21, 24)},    # 21-23 -> 8
         **{i: 9 for i in range(24, 26)},    # 24-25 -> 9
         **{i: 10 for i in range(26, 28)},   # 26-27 -> 10
         **{i: 11 for i in range(28, 30)},   # 28-29 -> 11
         **{i: 12 for i in range(30, 33)},   # 30-32 -> 12
         **{i: 13 for i in range(33, 35)},   # 33-34 -> 13
         **{i: 14 for i in range(35, 37)},   # 35-36 -> 14
         **{i: 15 for i in range(37, 40)},   # 37-39 -> 15
         **{i: 16 for i in range(40, 42)},   # 40-41 -> 16
         **{i: 17 for i in range(42, 44)},   # 42-43 -> 17
         **{i: 18 for i in range(44, 46)},   # 44-45 -> 18
         **{i: 19 for i in range(46, 50)},   # 46-49 -> 19
    },
    
    (11, 0, 9): {
         **{i: 1 for i in range(0, 8)},      # 0-7 -> 1
         **{i: 2 for i in range(8, 10)},     # 8-9 -> 2
         **{i: 3 for i in range(10, 12)},    # 10-11 -> 3
         **{i: 4 for i in range(12, 15)},    # 12-14 -> 4
         **{i: 5 for i in range(15, 17)},    # 15-16 -> 5
         **{i: 6 for i in range(17, 19)},    # 17-18 -> 6
         **{i: 7 for i in range(19, 22)},    # 19-21 -> 7
         **{i: 8 for i in range(22, 24)},    # 22-23 -> 8
         **{i: 9 for i in range(24, 26)},    # 24-25 -> 9
         **{i: 10 for i in range(26, 29)},   # 26-28 -> 10
         **{i: 11 for i in range(29, 31)},   # 29-30 -> 11
         **{i: 12 for i in range(31, 33)},   # 31-32 -> 12
         **{i: 13 for i in range(33, 35)},   # 33-34 -> 13
         **{i: 14 for i in range(35, 38)},   # 35-37 -> 14
         **{i: 15 for i in range(38, 40)},   # 38-39 -> 15
         **{i: 16 for i in range(40, 42)},   # 40-41 -> 16
         **{i: 17 for i in range(42, 44)},   # 42-43 -> 17
         **{i: 18 for i in range(44, 46)},   # 44-45 -> 18
         **{i: 19 for i in range(46, 50)},   # 46-49 -> 19
    },
   
   
    # These tables are for 10. Symbol Suche Task
    #
    (7, 2, 10): {
        **{i: 1 for i in range(0, 3)},      # 0-2 -> 1
        **{i: 2 for i in range(3, 6)},      # 3-5 -> 2
        **{i: 3 for i in range(6, 9)},      # 6-8 -> 3
        **{i: 4 for i in range(9, 13)},     # 9-12 -> 4
        **{i: 5 for i in range(13, 16)},    # 13-15 -> 5
        **{i: 6 for i in range(16, 19)},    # 16-18 -> 6
        **{i: 7 for i in range(19, 23)},    # 19-22 -> 7
        **{i: 8 for i in range(23, 26)},    # 23-25 -> 8
        **{i: 9 for i in range(26, 29)},    # 26-28 -> 9
        **{i: 10 for i in range(29, 32)},   # 29-31 -> 10
        **{i: 11 for i in range(32, 35)},   # 32-34 -> 11
        **{i: 12 for i in range(35, 37)},   # 35-36 -> 12
        **{i: 13 for i in range(37, 38)},   # 37-37 -> 13
        **{i: 14 for i in range(38, 40)},   # 38-39 -> 14
        **{i: 15 for i in range(40, 41)},   # 40-40 -> 15
        **{i: 16 for i in range(41, 42)},   # 41-41 -> 16
        **{i: 18 for i in range(42, 43)},   # 42-42 -> 18
    },
    
    (8, 0, 10): {
        **{i: 1 for i in range(0, 3)},      # 0-2 -> 1
        **{i: 2 for i in range(3, 5)},      # 3-4 -> 2
        **{i: 3 for i in range(5, 7)},      # 5-6 -> 3
        **{i: 4 for i in range(7, 9)},      # 7-8 -> 4
        **{i: 5 for i in range(9, 11)},     # 9-10 -> 5
        **{i: 6 for i in range(11, 13)},    # 11-12 -> 6
        **{i: 7 for i in range(13, 15)},    # 13-14 -> 7
        **{i: 8 for i in range(15, 17)},    # 15-16 -> 8
        **{i: 9 for i in range(17, 19)},    # 17-18 -> 9
        **{i: 10 for i in range(19, 21)},   # 19-20 -> 10
        **{i: 11 for i in range(21, 23)},   # 21-22 -> 11
        **{i: 12 for i in range(23, 25)},   # 23-24 -> 12
        **{i: 13 for i in range(25, 27)},   # 25-26 -> 13
        **{i: 14 for i in range(27, 29)},   # 27-28 -> 14
        **{i: 15 for i in range(29, 30)},   # 29-29 -> 15
        **{i: 16 for i in range(30, 31)},   # 30-30 -> 16
        **{i: 17 for i in range(31, 33)},   # 31-32 -> 17
        **{i: 18 for i in range(33, 35)},   # 33-34 -> 18
        **{i: 19 for i in range(35, 61)},   # 35-60 -> 19
    },
    
    (8, 1, 10): {
        **{i: 1 for i in range(0, 4)},      # 0-3 -> 1
        **{i: 2 for i in range(4, 6)},      # 4-5 -> 2
        **{i: 3 for i in range(6, 8)},      # 6-7 -> 3
        **{i: 4 for i in range(8, 10)},     # 8-9 -> 4
        **{i: 5 for i in range(10, 12)},    # 10-11 -> 5
        **{i: 6 for i in range(12, 14)},    # 12-13 -> 6
        **{i: 7 for i in range(14, 16)},    # 14-15 -> 7
        **{i: 8 for i in range(16, 18)},    # 16-17 -> 8
        **{i: 9 for i in range(18, 20)},    # 18-19 -> 9
        **{i: 10 for i in range(20, 22)},   # 20-21 -> 10
        **{i: 11 for i in range(22, 24)},   # 22-23 -> 11
        **{i: 12 for i in range(24, 26)},   # 24-25 -> 12
        **{i: 13 for i in range(26, 28)},   # 26-27 -> 13
        **{i: 14 for i in range(28, 30)},   # 28-29 -> 14
        **{i: 15 for i in range(30, 31)},   # 30-30 -> 15
        **{i: 16 for i in range(31, 32)},   # 31-31 -> 16
        **{i: 17 for i in range(32, 34)},   # 32-33 -> 17
        **{i: 18 for i in range(34, 36)},   # 34-35 -> 18
        **{i: 19 for i in range(36, 61)},   # 36-60 -> 19
    },
    
    (8, 2, 10): {
        **{i: 1 for i in range(0, 4)},      # 0-3 -> 1
        **{i: 2 for i in range(4, 7)},      # 4-6 -> 2
        **{i: 3 for i in range(7, 9)},      # 7-8 -> 3
        **{i: 4 for i in range(9, 11)},     # 9-10 -> 4
        **{i: 5 for i in range(11, 13)},    # 11-12 -> 5
        **{i: 6 for i in range(13, 15)},    # 13-14 -> 6
        **{i: 7 for i in range(15, 17)},    # 15-16 -> 7
        **{i: 8 for i in range(17, 19)},    # 17-18 -> 8
        **{i: 9 for i in range(19, 21)},    # 19-20 -> 9
        **{i: 10 for i in range(21, 23)},   # 21-22 -> 10
        **{i: 11 for i in range(23, 25)},   # 23-24 -> 11
        **{i: 12 for i in range(25, 27)},   # 25-26 -> 12
        **{i: 13 for i in range(27, 29)},   # 27-28 -> 13
        **{i: 14 for i in range(29, 31)},   # 29-30 -> 14
        **{i: 15 for i in range(31, 32)},   # 31-31 -> 15
        **{i: 16 for i in range(32, 33)},   # 32-32 -> 16
        **{i: 17 for i in range(33, 35)},   # 33-34 -> 17
        **{i: 18 for i in range(35, 37)},   # 35-36 -> 18
        **{i: 19 for i in range(37, 61)},   # 37-60 -> 19
    },
    
    (9, 0, 10): {
        **{i: 1 for i in range(0, 5)},      # 0-4 -> 1
        **{i: 2 for i in range(5, 7)},      # 5-6 -> 2
        **{i: 3 for i in range(7, 9)},      # 7-8 -> 3
        **{i: 4 for i in range(9, 12)},     # 9-11 -> 4
        **{i: 5 for i in range(12, 14)},    # 12-13 -> 5
        **{i: 6 for i in range(14, 16)},    # 14-15 -> 6
        **{i: 7 for i in range(16, 18)},    # 16-17 -> 7
        **{i: 8 for i in range(18, 20)},    # 18-19 -> 8
        **{i: 9 for i in range(20, 22)},    # 20-21 -> 9
        **{i: 10 for i in range(22, 24)},   # 22-23 -> 10
        **{i: 11 for i in range(24, 26)},   # 24-25 -> 11
        **{i: 12 for i in range(26, 28)},   # 26-27 -> 12
        **{i: 13 for i in range(28, 30)},   # 28-29 -> 13
        **{i: 14 for i in range(30, 32)},   # 30-31 -> 14
        **{i: 15 for i in range(32, 33)},   # 32-32 -> 15
        **{i: 16 for i in range(33, 34)},   # 33-33 -> 16
        **{i: 17 for i in range(34, 36)},   # 34-35 -> 17
        **{i: 18 for i in range(36, 38)},   # 36-37 -> 18
        **{i: 19 for i in range(38, 61)},   # 38-60 -> 19
    },
    
    (9, 1, 10): {
        **{i: 1 for i in range(0, 5)},      # 0-4 -> 1
        **{i: 2 for i in range(5, 8)},      # 5-7 -> 2
        **{i: 3 for i in range(8, 10)},     # 8-9 -> 3
        **{i: 4 for i in range(10, 12)},    # 10-11 -> 4
        **{i: 5 for i in range(12, 15)},    # 12-14 -> 5
        **{i: 6 for i in range(15, 17)},    # 15-16 -> 6
        **{i: 7 for i in range(17, 19)},    # 17-18 -> 7
        **{i: 8 for i in range(19, 21)},    # 19-20 -> 8
        **{i: 9 for i in range(21, 23)},    # 21-22 -> 9
        **{i: 10 for i in range(23, 25)},   # 23-24 -> 10
        **{i: 11 for i in range(25, 27)},   # 25-26 -> 11
        **{i: 12 for i in range(27, 29)},   # 27-28 -> 12
        **{i: 13 for i in range(29, 31)},   # 29-30 -> 13
        **{i: 14 for i in range(31, 33)},   # 31-32 -> 14
        **{i: 15 for i in range(33, 34)},   # 33-33 -> 15
        **{i: 16 for i in range(34, 35)},   # 34-34 -> 16
        **{i: 17 for i in range(35, 37)},   # 35-36 -> 17
        **{i: 18 for i in range(37, 39)},   # 37-38 -> 18
        **{i: 19 for i in range(39, 61)},   # 39-60 -> 19
    },
    
    (9, 2, 10): {
        **{i: 1 for i in range(0, 5)},      # 0-4 -> 1
        **{i: 2 for i in range(5, 8)},      # 5-7 -> 2
        **{i: 3 for i in range(8, 10)},     # 8-9 -> 3
        **{i: 4 for i in range(10, 13)},    # 10-12 -> 4
        **{i: 5 for i in range(13, 15)},    # 13-14 -> 5
        **{i: 6 for i in range(15, 17)},    # 15-16 -> 6
        **{i: 7 for i in range(17, 20)},    # 17-19 -> 7
        **{i: 8 for i in range(20, 22)},    # 20-21 -> 8
        **{i: 9 for i in range(22, 24)},    # 22-23 -> 9
        **{i: 10 for i in range(24, 26)},   # 24-25 -> 10
        **{i: 11 for i in range(26, 28)},   # 26-27 -> 11
        **{i: 12 for i in range(28, 30)},   # 28-29 -> 12
        **{i: 13 for i in range(30, 32)},   # 30-31 -> 13
        **{i: 14 for i in range(32, 34)},   # 32-33 -> 14
        **{i: 15 for i in range(34, 35)},   # 34-34 -> 15
        **{i: 16 for i in range(35, 36)},   # 35-35 -> 16
        **{i: 17 for i in range(36, 38)},   # 36-37 -> 17
        **{i: 18 for i in range(38, 40)},   # 38-39 -> 18
        **{i: 19 for i in range(39, 61)},   # 39-60 -> 19
    },
    
    (10, 0, 10): {
        **{i: 1 for i in range(0, 6)},      # 0-5 -> 1
        **{i: 2 for i in range(6, 8)},      # 6-7 -> 2
        **{i: 3 for i in range(8, 10)},     # 8-9 -> 3
        **{i: 4 for i in range(10, 13)},    # 10-12 -> 4
        **{i: 5 for i in range(13, 16)},    # 13-15 -> 5
        **{i: 6 for i in range(16, 18)},    # 16-17 -> 6
        **{i: 7 for i in range(18, 20)},    # 18-19 -> 7
        **{i: 8 for i in range(20, 23)},    # 20-22 -> 8
        **{i: 9 for i in range(23, 25)},    # 23-24 -> 9
        **{i: 10 for i in range(25, 27)},   # 25-26 -> 10
        **{i: 11 for i in range(27, 29)},   # 27-28 -> 11
        **{i: 12 for i in range(29, 31)},   # 29-30 -> 12
        **{i: 13 for i in range(31, 33)},   # 31-32 -> 13
        **{i: 14 for i in range(33, 35)},   # 33-34 -> 14
        **{i: 15 for i in range(35, 36)},   # 35-35 -> 15
        **{i: 16 for i in range(36, 37)},   # 36-36 -> 16
        **{i: 17 for i in range(37, 39)},   # 37-38 -> 17
        **{i: 18 for i in range(39, 41)},   # 39-40 -> 18
        **{i: 19 for i in range(41, 61)},   # 41-60 -> 19
    },
    
    (10, 1, 10): {
        **{i: 1 for i in range(0, 6)},      # 0-5 -> 1
        **{i: 2 for i in range(6, 9)},      # 6-8 -> 2
        **{i: 3 for i in range(9, 11)},     # 9-10 -> 3
        **{i: 4 for i in range(11, 14)},    # 11-13 -> 4
        **{i: 5 for i in range(14, 16)},    # 14-15 -> 5
        **{i: 6 for i in range(16, 19)},    # 16-18 -> 6
        **{i: 7 for i in range(19, 21)},    # 19-20 -> 7
        **{i: 8 for i in range(21, 23)},    # 21-22 -> 8
        **{i: 9 for i in range(23, 25)},    # 23-24 -> 9
        **{i: 10 for i in range(25, 28)},   # 25-27 -> 10
        **{i: 11 for i in range(28, 30)},   # 28-29 -> 11
        **{i: 12 for i in range(30, 32)},   # 30-31 -> 12
        **{i: 13 for i in range(32, 34)},   # 32-33 -> 13
        **{i: 14 for i in range(34, 35)},   # 34-34 -> 14
        **{i: 15 for i in range(35, 37)},   # 35-36 -> 15
        **{i: 16 for i in range(37, 38)},   # 37-37 -> 16
        **{i: 17 for i in range(38, 40)},   # 38-39 -> 17
        **{i: 18 for i in range(40, 42)},   # 40-41 -> 18
        **{i: 19 for i in range(41, 61)},   # 41-60 -> 19
    },
    
    (10, 2, 10): {
        **{i: 1 for i in range(0, 6)},      # 0-5 -> 1
        **{i: 2 for i in range(6, 9)},      # 6-8 -> 2
        **{i: 3 for i in range(9, 11)},     # 9-10 -> 3
        **{i: 4 for i in range(11, 14)},    # 11-13 -> 4
        **{i: 5 for i in range(14, 17)},    # 14-16 -> 5
        **{i: 6 for i in range(17, 19)},    # 17-18 -> 6
        **{i: 7 for i in range(19, 21)},    # 19-20 -> 7
        **{i: 8 for i in range(21, 24)},    # 21-23 -> 8
        **{i: 9 for i in range(24, 26)},    # 24-25 -> 9
        **{i: 10 for i in range(26, 28)},   # 26-27 -> 10
        **{i: 11 for i in range(28, 30)},   # 28-29 -> 11
        **{i: 12 for i in range(30, 32)},   # 30-31 -> 12
        **{i: 13 for i in range(32, 34)},   # 32-33 -> 13
        **{i: 14 for i in range(34, 36)},   # 34-35 -> 14
        **{i: 15 for i in range(36, 38)},   # 36-37 -> 15
        **{i: 16 for i in range(38, 39)},   # 38-38 -> 16
        **{i: 17 for i in range(39, 41)},   # 39-40 -> 17
        **{i: 18 for i in range(41, 43)},   # 41-42 -> 18
        **{i: 19 for i in range(43, 61)},   # 43-60 -> 19
    },
    
    (11, 0, 10): {
        **{i: 1 for i in range(0, 7)},      # 0-6 -> 1
        **{i: 2 for i in range(7, 9)},      # 7-8 -> 2
        **{i: 3 for i in range(9, 12)},     # 9-11 -> 3
        **{i: 4 for i in range(12, 15)},    # 12-14 -> 4
        **{i: 5 for i in range(15, 17)},    # 15-16 -> 5
        **{i: 6 for i in range(17, 20)},    # 17-19 -> 6
        **{i: 7 for i in range(20, 22)},    # 20-21 -> 7
        **{i: 8 for i in range(22, 24)},    # 22-23 -> 8
        **{i: 9 for i in range(24, 27)},    # 24-26 -> 9
        **{i: 10 for i in range(27, 29)},   # 27-28 -> 10
        **{i: 11 for i in range(29, 31)},   # 29-30 -> 11
        **{i: 12 for i in range(31, 33)},   # 31-32 -> 12
        **{i: 13 for i in range(33, 35)},   # 33-34 -> 13
        **{i: 14 for i in range(35, 37)},   # 35-36 -> 14
        **{i: 15 for i in range(37, 39)},   # 37-38 -> 15
        **{i: 16 for i in range(39, 40)},   # 39-39 -> 16
        **{i: 17 for i in range(40, 42)},   # 40-41 -> 17
        **{i: 18 for i in range(42, 44)},   # 42-43 -> 18
        **{i: 19 for i in range(43, 61)},   # 43-60 -> 19
    }
   

}

