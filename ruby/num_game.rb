min = 0
max = 100
puts "please input a integer between %d and %d" % [min, max]
result = rand(max)
while num = gets().to_i
    if num > result
        puts "your input is a little big, please try again"
    elsif num < result
        puts "your input is a little small, please try again"
    elsif num == result
        puts "congratulations!"
        break
    end
end
