# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:45:57 2025
This is the conversion Tables
@author: Liu
"""
# List of conversion tables
conversion_tables = {
    (7, 2, 4): {
        0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2,  # 0-5 -> 1
        7: 3,  # 6 -> 2
        8: 3, 9: 4,  # 7-8 -> 3
        10: 4, 11: 5,  # 9-10 -> 4
        12: 5, 13: 6,  # 11-12 -> 5
        14: 6,  # 13-14 -> 6
        15: 7, 16: 8,  # 15 -> 7
        17: 8, 18:98,  # 16-17 -> 8
        19: 9,  # 18-19 -> 9
        20: 10, 21: 11,  # 20 -> 10
        22: 11, 23: 12,  # 21-22 -> 11
        24: 12,  # 23-24 -> 12
        25: 13, 26: 14,  # 25 -> 13
        27: 14, 28: 15,  # 26-27 -> 14
        29: 16,  # 28 -> 15
        30: 16, 31: 17,  # 29-30 -> 16
        32: 17, 33: 18,  # 31-32 -> 17
         # 33 -> 18
        # 34-54 -> 19
        **{i: 19 for i in range(34, 55)}  
    },
    (8, 0, 4): {
        0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1,  # 0-6 -> 1
        7: 2,  # 7 -> 2
        8: 3, 9: 3,  # 8-9 -> 3
        10: 4, 11: 4,  # 10-11 -> 4
        12: 5, 13: 5,  # 12-13 -> 5
        14: 6,  # 14 -> 6
        15: 7, 16: 7,  # 15-16 -> 7
        17: 8, 18: 8,  # 17-18 -> 8
        19: 9,  # 19 -> 9
        20: 10, 21: 10,  # 20-21 -> 10
        22: 11, 23: 11,  # 22-23 -> 11
        24: 12,  # 24 -> 12
        25: 13, 26: 13,  # 25-26 -> 13
        27: 14, 28: 14,  # 27-28 -> 14
        29: 15,  # 29 -> 15
        30: 16, 31: 16,  # 30-31 -> 16
        32: 17, 33: 17,  # 32-33 -> 17
        34: 18,  # 34 -> 18
        # 35-54 -> 19
        **{i: 19 for i in range(35, 55)}  
    },
    (8, 1, 4): {
        0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1,  # 0-6 -> 1
        7: 2, 8: 2, # 7-8 -> 2
        9: 3, 10: 3,  # 9-10 -> 3
        11: 4, 12: 4,  # 11-12 -> 4
        13: 5,  # 13 -> 5
       
        14: 6,  # 14-15 -> 6
        15: 6, 16: 7,  # 16-17 -> 7
        17: 7, 18: 8,  # 18 -> 8
        19: 9,  # 19-20 -> 9
        20: 9, 21: 10,  # 21-22 -> 10
        22: 10, 
        
        23: 11,  # 23-24 -> 11
        24: 11,  # 25 -> 12
        25: 12, 26: 13,  # 26-27 -> 13
        27: 13, 28: 14,  # 28-29 -> 14
        29: 14,  # 30 -> 15
        30: 15, 
        
        31: 16,  # 31-32 -> 16
        32: 16, 33: 17,  # 33 -> 17
        34: 18, 35: 18  # 34-35 -> 18
        # 36-54 -> 19
        **{i: 19 for i in range(36, 55)}  
    },
    (8, 2, 4): {
        0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1,  # 0-7 -> 1
        7: 1, 8: 2, # 8-9 -> 2
        9: 2, 10: 3,  # 10 -> 3
        11: 4, 12: 4,  # 11-12 -> 4
        13: 5, 14: 5,  # 13-14 -> 5
       
        15: 6,  # 15-16 -> 6
        16: 6,  # 17 -> 7
        17: 7, 18: 8,  # 18-19 -> 8
        19: 8,  # 20-21 -> 9
        20: 9, 21: 9,  # 22-23 -> 10
        22: 10, 23: 10,
        
        # 24 -> 11
        24: 11,  # 25-26 -> 12
        25: 12, 26: 12,  # 27-28 -> 13
        27: 13, 28: 13,  # 29 -> 14
        29: 14,  # 30-31 -> 15
        30: 15, 31: 15,
        
        32: 16,  # 32-33 -> 16
        33: 16, 34: 17,  # 34 -> 17
        35: 18, 36: 18  # 35-36 -> 18
        # 37-54 -> 19
        **{i: 19 for i in range(37, 55)}  
    },  
    (9, 0, 4): {
        0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1,  # 0-7 -> 1
        7: 1, 8: 2, # 8-9 -> 2
        9: 2, 10: 3,  # 10-11 -> 3
        11: 2, 12: 4,  # 12-13 -> 4
        13: 4, 14: 5,  # 14 -> 5
       
        15: 6, 16: 6, # 15-16 -> 6
        17: 7, 18: 7,  # 17-18 -> 7
        19: 8, 20: 8, # 19-20 -> 8
        21: 9,  # 21 -> 9
        22: 10, 23: 10,  # 22-23 -> 10
       
        24: 11, 25: 11,# 24-25 -> 11
        26: 12, # 26 -> 12
        27: 13, 28: 13,  # 27-28 -> 13
        29: 14,  # 29-30 -> 14
        30: 14, 31: 15, 32: 15, # 31-32 -> 15
       
        33: 16,  # 33 -> 16
        34: 17, 35: 17,  # 34-35 -> 17
        36: 18  # 36 -> 18
        # 37-54 -> 19
        **{i: 19 for i in range(37, 55)}  
    },  
    (9, 1, 4): {
        0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, # 0-8 -> 1
        9: 2, 10: 2,  # 9-10 -> 2
        11: 3, # 11 -> 3
        12: 4, 13: 4, # 12-13 -> 4
        14: 5, 15: 5,# 14-15 -> 5
       
        16: 6, # 16-17 -> 6
        17: 6, 18: 7,  # 18 -> 7
        19: 8, 20: 8, # 19-20 -> 8
        21: 9, 22: 9, # 21-22 -> 9
        23: 10,  24: 10,# 23-24 -> 10
       
        25: 11,# 25 -> 11
        26: 12, # 26-27 -> 12
        27: 12, 28: 13,  # 28-29 -> 13
        29: 13,  # 30 -> 14
        30: 14, 31: 15, 32: 15, # 31-32 -> 15
       
        33: 16,  # 33-34 -> 16
        34: 16, 35: 17,  # 34-35 -> 17
        36: 18, 37: 18  # 36-37 -> 18
        # 38-54 -> 19
        **{i: 19 for i in range(38, 55)}  
    }, 
    (9, 2, 4): {
        0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, # 0-8 -> 1
        9: 2, 10: 2,  # 9-10 -> 2
        11: 3, # 11-12 -> 3
        12: 3, 13: 4, # 12-13 -> 4
        14: 4, 15: 5,# 14-15 -> 5
       
        16: 6, # 16-17 -> 6
        17: 6, 18: 7,  # 18-19 -> 7
        19: 7, 20: 8, # 20-21 -> 8
        21: 8, 22: 9, # 22 -> 9
        23: 10,  24: 10, # 23-24 -> 10
       
        25: 11, 26: 11, # 25-26 -> 11
        27: 12, # 27 -> 12
        28: 13, 29: 13, # 28-29 -> 13
        30: 14, 31: 14,  # 30-31 -> 14
        32: 15, 33: 15, # 32-33 -> 15
       
        34: 16,  # 34 -> 16
        35: 17, 36: 17,  # 35-36 -> 17
        37: 18, 38: 18  # 37-38 -> 18
        # 39-54 -> 19
        **{i: 19 for i in range(39, 55)}  
    },
    (10, 0, 4): {
        0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, # 0-9 -> 1
        10: 2, 11: 3,# 10 -> 2
        # 11-12 -> 3
        12: 3, 13: 4, # 13-14 -> 4
        14: 4, 15: 5, 16: 5,# 15-16 -> 5
       
        # 17 -> 6
        17: 6, 18: 7,  # 18-19 -> 7
        19: 7, 20: 8, # 20-21 -> 8
        21: 8, 22: 9, # 22-23 -> 9
        23: 9,  24: 10, # 24 -> 10
       
        25: 11, 26: 11, # 25-26 -> 11
        27: 12, # 27-28 -> 12
        28: 12, 29: 13, # 29-30 -> 13
        30: 13, 31: 14,  # 31 -> 14
        32: 15, 33: 15, # 32-33 -> 15
       
        34: 16,  # 34-35 -> 16
        35: 16, 36: 17,  # 36 -> 17
        37: 18, 38: 18  # 37-38 -> 18
        # 39-54 -> 19
        **{i: 19 for i in range(39, 55)}  
    }, 
    (10, 1, 4): {
        0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, # 0-9 -> 1
        10: 2, 11: 2,# 10-11 -> 2
        # 12 -> 3
        12: 3, 13: 4, # 13-14 -> 4
        14: 4, 15: 5, 16: 5,# 15-16 -> 5
       
        17: 6, 18: 6, # 17-18 -> 6
        19: 7,  # 19 -> 7
        20: 8, 21: 8, # 20-21 -> 8
        22: 9, 23: 9, # 22-23 -> 9
        24: 10, 25: 10, # 24-25 -> 10
       
        26: 11, # 26 -> 11
        27: 12, # 27-28 -> 12
        28: 12, 29: 13, # 29-30 -> 13
        30: 13, 31: 14,  # 31-32 -> 14
        32: 14, 33: 15, # 33 -> 15
       
        34: 16, 35: 16, # 34-35 -> 16
        36: 17, 37: 17, # 36-37 -> 17
        38: 18, 39: 18  # 38-39 -> 18
        # 40-54 -> 19
        **{i: 19 for i in range(40, 55)}  
    }, 
    (10, 2, 4): {
        0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, # 0-9 -> 1
        10: 2, 11: 2,# 10-11 -> 2
        # 12-13 -> 3
        12: 3, 13: 3, # 14 -> 4
        14: 4, 15: 5, 16: 5,# 15-16 -> 5
       
        17: 6, 18: 6, # 17-18 -> 6
        19: 7,  # 19-20 -> 7
        20: 7, 21: 8, # 21 -> 8
        22: 9, 23: 9, # 22-23 -> 9
        24: 10, 25: 10, # 24-25 -> 10
       
        26: 11, # 26-27 -> 11
        27: 11, # 28 -> 12
        28: 12, 29: 13, # 29-30 -> 13
        30: 13, 31: 14,  # 31-32 -> 14
        32: 14, 33: 15, # 33-34 -> 15
       
        34: 15, 35: 16, # 35 -> 16
        36: 17, 37: 17, # 36-37 -> 17
        38: 18, 39: 18  # 38-39 -> 18
        # 40-54 -> 19
        **{i: 19 for i in range(40, 55)}  
    }, 

}
