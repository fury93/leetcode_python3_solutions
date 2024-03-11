class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        match freq:
            case 'minute': delta = 60
            case 'hour': delta = 3600
            case _: delta = 86400

        results = [0 for _ in range(startTime, endTime+1, delta)]
        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                results[(time-startTime) // delta] += 1
        
        return results


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)