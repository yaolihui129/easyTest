# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。


def isPalindrome(yyyy):
	if not isinstance(yyyy,str):
		yyyy=str(yyyy)
	l =len(yyyy)

	if l%2==0:
		ll=l//2
	else:
		ll=(l-1)//2

	for x in range(ll):
		if yyyy[x]!=yyyy[l-1-x]:
			return False
	return True


print(isPalindrome(1))
