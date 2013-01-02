module foo

use iso_c_binding

implicit none

contains

    integer(c_int) function multiply(a, b) bind(c)
        integer(c_int), intent(in) :: a,b
        multiply = a*b
    end function multiply

    integer(c_int) function addtwo(a, b) bind(c)
        integer(c_int), intent(in) :: a,b
        addtwo = a+b
    end function addtwo

    real(c_double) function addtwo_real(a, b) bind(c)
        real(c_double), intent(in) :: a,b
        addtwo_real = a+b
    end function addtwo_real

    subroutine times_row(mat, rows, columns) bind(c)
        real(c_double), dimension(*) ,intent(inout) :: mat
        integer(c_int), intent(in) :: rows, columns
        integer :: i,j, idx
        
        do i=1,rows
            do j=1,columns
                idx = (i-1)*columns + j
                mat(idx) = mat(idx) * (i-1)
            enddo
        enddo
    endsubroutine

end module
