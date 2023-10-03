#!/usr/bin/env ruby
# A regular expression that matches hbtn with
# zero or more instances of "t"

puts ARGV[0].scan(/hbt*n/).join
