import numpy as np

array = [ 1 , 17 , 5 , 10 , 13 , 15 , 10 , 5 , 16 , 8 ]

array2 = np.array ( array )
unique_array = np.unique ( array2 )

swap_index = int ( len ( unique_array ) / 2 )

unique_array .sort ()
        
if swap_index < len ( unique_array ) / 2 :
    swap_index += 1

for index in range ( 0 , int ( len ( unique_array ) / 2 ) + 1 , 2 ) :

    if ( swap_index + index >= len ( unique_array ) or swap_index - index < 0 ) : break

    temp = unique_array [ swap_index + index ]
    unique_array [ swap_index + index ] = unique_array [ swap_index - index - 1 ]
    unique_array [ swap_index - index - 1 ] = temp

print ( unique_array )