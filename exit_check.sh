git diff --exit-code
if [$? == 0]
then
	echo "there is no changes"
else
	echo "there is changes"
fi
