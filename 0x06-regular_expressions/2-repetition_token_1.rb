#!/usr/bin/env ruby
# A regular expression that matches hbtn with zero or one
# instance of "b"

puts ARGV[0].scan(/hb?tn/).join
