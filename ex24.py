print "Let's practice everything."
print 'You\'d need to know \'bout escpaes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n needs fo love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none
"""

print "---------"
print poem
print "----------"
five = 10 - 2 + 3
print  "This should be five:%s" % five

def secret_formula(started):
	jelly_beans = starrted * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,jars,crates
	
start_point = 10000
# beans, jars, crates = secret_formula(start_point)
# print "With a starting point of:%d" % 