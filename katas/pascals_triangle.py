def generate(numRows):
        output = []
        for i in range(1, numRows + 1):
            output.append([1] * i)
        for i in range(2, numRows+1):
            for j in range(1, len(output[i-1])-1):
                #print(output[i-1][j])
                output[i-1][j] = output[i-2][j-1] + output[i-2][j]
        return output
            