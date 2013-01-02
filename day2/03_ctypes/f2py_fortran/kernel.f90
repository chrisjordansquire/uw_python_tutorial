module foo

implicit none

contains

    integer function multiply(a, b)
        integer, intent(in) :: a,b
        multiply = a*b
    end function multiply

    integer function addtwo(a, b) 
        integer, intent(in) :: a,b
        addtwo = a+b
    end function addtwo

    real function addtwo_real(a,b)
        real, intent(in) :: a,b
        addtwo_real = a+b
    end function addtwo_real

    subroutine times_row(mat, rows, columns) 
        !Must change intent(out) to intent(in) for f2py 
        !to handle correctly
        real, dimension(*) ,intent(inout) :: mat
        integer, intent(in) :: rows, columns
        integer :: i,j, idx
        
        do i=1,rows
            do j=1,columns
                idx = (i-1)*columns + j
                mat(idx) = mat(idx) * (i-1)
            enddo
        enddo
    endsubroutine

end module
