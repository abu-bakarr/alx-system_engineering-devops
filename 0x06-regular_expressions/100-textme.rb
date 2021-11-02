#!/usr/bin/env ruby
FROM =  ARGV[0].scan(/(?<=from:)\S+\b/).join
TO = ARGV[0].scan(/(?<=to:)\S+\b/).join
FLAG = ARGV[0].scan(/(?<=flags:)\S+\b/).join
puts (FROM + "," + TO + "," + FLAG)
