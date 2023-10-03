#!/usr/bin/env ruby
# A regular expression that matches hbtn with
# at least an instance of "t"

puts ARGV[0].scan(/hbt+n/).join
