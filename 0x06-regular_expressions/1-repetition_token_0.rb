#!/usr/bin/env ruby
# A regular expression that matches hbtn with at least
# 2Ts and 5 Ts at most

puts ARGV[0].scan(/hbt{2,5}n/).join
