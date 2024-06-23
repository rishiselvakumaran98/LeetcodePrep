import time
class TokenBucket:

    """
    We implement a simple Token Bucket Application using this 
    """
    def __init__(self, BucketSize, refillRate) -> None:
        self.bucketSize = BucketSize
        self.refillRate = refillRate
        self.lastRefillTime = time.time()
        self.currentBucketSize = BucketSize

    def allowRequest(self, tokens):
        """
        This method allows requests to be made if there are enough tokens in the bucket
        """
        self.refill()
        if tokens <= self.currentBucketSize:
            self.currentBucketSize -= tokens
            return True
        return False
    
    def refill(self):
        """
        This method refills the bucket with tokens
        """
        currentTime = time.time()
        tokensToAdd = ((currentTime - self.lastRefillTime) * self.refillRate) // 10**9
        self.currentBucketSize = min(self.currentBucketSize + tokensToAdd, self.bucketSize)
        self.lastRefillTime = currentTime


    
