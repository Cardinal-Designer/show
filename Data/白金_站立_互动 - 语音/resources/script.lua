i_cnt = 73
r_cnt = 121
file1_sep = "/R/F (ID).png"
file2_sep = "/I/F (ID).png"

isClick = false
numClick = 1

function OnClick()
	isClick = true
end

function init()
	for i=1, r_cnt do LoadBitmap((string.gsub(file1_sep, "ID", i))) end
	for i=1, i_cnt do LoadBitmap((string.gsub(file2_sep, "ID", i))) end
	RequestClickEvent("OnClick")
end

i=0
function update()
	DisplayBitmap(i)
	i = i + 1
	if(i >= r_cnt + i_cnt) then
		i = 0
		isClick = false
	end
	if(i == r_cnt) then
		i = 0
	end
        if(isClick and i < r_cnt and numClick % 10 ~= 0) then
		PlaySound("click1.wav")
		i = r_cnt
                numClick = numClick + 1
	end
	if(isClick and i < r_cnt and numClick % 10 == 0) then
		PlaySound("click2.wav")
		i = r_cnt
                numClick = numClick + 1
	end
	return 1.0 / 60
end