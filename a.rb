require 'linkedin-scraper'


puts "Hello World!"

profile = Linkedin::Profile.new("http://www.linkedin.com/in/jeffweiner08")

puts profile.first_name 