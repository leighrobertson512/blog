Title: FORTRAN and CoffeeScript
Date: 2015-03-11
Category: General
Tags: FORTRAN, coffeescript, binary logic, half-adder
Author: Wray Mills
Summary: A week in the life...

### Language Elegance

What does FORTRAN and CoffeeScript have in common? Well, aside from
being programming languages (of course, there could be some arguments
about formal languages vs. scripting languages vs. meta-scripting
language -- just humor me for now), not much. But, I have the
"pleasure" of working on a project that is using both. And, in fact,
in a horrible violation of DRY, we are currently defining probability
distributions and prob. dist. approximations in both! This will change soon; however, for now, it
makes the project kind of cool. Its like the best and worst of
old-school and new school. One can actually learn from reviewing dated
FORTRAN code just as one can learn from the CoffeeScript and actually
cross-leverage some concepts. Regardless, one can't help but
appreciate the elegance of the CoffeeScript compared with the
FORTRAN. Check this out:

#### FORTRAN
```FORTRAN
!   Creating the Normal Approximation function. For now, we are using this from the shell.f module for the
!   Gaussian distributions.
	RECURSIVE FUNCTION normal_approx(z)
	  IMPLICIT NONE
	  REAL(KIND=8),INTENT(IN) :: z
	  REAL(KIND=8) :: normal_approx
	  INTEGER :: i

!     if z is less than 0, then the value above is equal
!     to 1 - Q(-z), so return 1 - temp
      IF(z < 0) THEN
		 normal_approx = 1 - normal_approx(-1*z)
      END IF


!     calculate the number according to the polynomial (these should be constants)
      normal_approx = (1.0 - 0.5 * ((1.0 + 0.0498673470 * z
     1                        	+ 0.0211410061*z*z + 
     2                          0.0032776263*(z**3) + 
     3                          0.0000380036*(z**4) +
     4                          0.0000488906*(z**5) +
     5                          0.0000053830*(z**6)) **(-16))) 

!     verify that the number is within the computational
!     limits of the dist_r 
      IF(normal_approx < (10.0 **(-16)))THEN
		 normal_approx = (10.0 **(-16))
      END IF
      IF((normal_approx > (1 - (10.0 **(-6)))).AND.(
     1   normal_approx < 1))THEN
         normal_approx = 1 - (10.0 **(-6))
      END IF

	  WRITE(UNIT=9,FMT=*) "normal approx at ", z, " is ",
     2	  normal_approx
	  
	END FUNCTION

```

#### Coffeescript

Granted, this could use a little more comments. But, it essentially
looks just like the definition for the Normal Approximation in the
textbook, so we can simply reference the section in the function definition comment.

```Javascript
Q = (z) ->
    return 1 - Q(- z) if z < 0

    return 0.5 if z == 0

    b = [1, 0.0498673470, 0.0211410061,
            0.0032776263, 0.0000380036,
            0.0000488906, 0.0000053830]
    acc = 0
    for i in [0..6]
        acc += b[i] * Math.pow(z, i)
    return 1 - Math.pow(acc, -16) / 2

```

### Digital Logic Design

Oh, and just to make the week even more well-rounded (in a Comp
Sci. sense), I've had a couple of my elementary classes working
through the binary number system, basic logic gates to form
half-adders to form full-adders to perform multi-digit binary
arithmetic! All this provides a nice setup for their Arduino sketches
for a microcontroller to control an 8x8 LED matrix.


### Minecraft, Arduino, Python, FORTRAN, C, Ruby, and Coffeescript for
#### LED controllers, minecraft server mods, enrollment systems, and
#### probabilistic distribution fitting engines

And actually even a few more languages/tasks in between. So, actually, if every week could be this cool, that
would be awesome. In fact, what makes this even better is that I get
to share a lot of this with our next generation of Software
Engineers. It's extremely rewarding to see such young students "coding"
away in Python or even writing out bytes in bits for an Arduino sketch
--  yes, 3rd graders defining bytes using bits in C. And to have an
intern who is still just a sophomore in high school defining multiple
ruby on rails environments (and all the related excruciating
regression testing getting all the gems at the right versions) who can
do such a task with very, very little guidance from me! And to work
with an undergrad on a graduate-level project who is such a gifted
coder in the most modern languages (like CoffeeScript) and who is
headed to Microsoft this year, makes me very comfortable with the
future of technology in the US!!
