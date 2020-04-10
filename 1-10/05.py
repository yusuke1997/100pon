class ngram:


    def ngram(target,n=1):
        #target is list type
        #return is list type
        #default is unigram
        result=[]
        for i in range(len(target)-n+1):
            result.append(target[i:i+n])
        
        return result



if __name__ == "__main__":

    tar="I am an NLPer"
    tar2=tar.split(" ")
    print(ngram.ngram(tar2,n=2))
