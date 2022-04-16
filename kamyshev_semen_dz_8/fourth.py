def val_checker(l_func):
   def val_checke(func):
      def val_check(num):
         if l_func(num):
            res = func(num)
         else:
            raise ValueError
         return res

      return val_check
   return val_checke



@val_checker(lambda x: x > 0)

def calc_cube(x):
   return x ** 3


print(calc_cube(5))
