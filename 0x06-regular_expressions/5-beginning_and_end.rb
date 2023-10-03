#!/usr/bin/env ruby
# A regular expression that matches a string
# that starts with "h" and ends with "n" with
# exactly one character in-between

puts ARGV[0].scan(/h.n/).join
