class Solution:

    def solve(self, A):

        dp = [0] * (len(A) + 1)
        last = [-1] * 256

        dp[0] = 1

        for i in range(1, len(A) + 1):
            dp[i] = (2 * dp[i - 1])
            l = ord(A[i - 1])

            if last[l] != -1:
                dp[i] = dp[i] - dp[last[l]]

            try:
                last[l] = (i - 1)
            except:
                print('exc')

        return (dp[len(A)] - 1) % 1000000007

A = "pgvmshqtdstnosagfssurajyyxbzrqhielavlcdzvwmwosakadvmropxpurscgyyeezgmnawgqxurrsvtpisgkkjcavffmclxnyxqvxjilnhuojuhstqemveslxnctmuneniiarllvoivrhvajqerdunpymepgiwbvmacsengmkjdxmnwgslnivitqdwdxuqidwikvcicuseouceyektexrotraandzliakovxmticegxuiffzjfgumogsfcfhhkisaamexiykgezlxcbvkixtmcdpaxsqpzzlwhqkqqaibgodggnekzhaywshssvjhhdbubcthiintspjugakcbiiavzmuscmzgplbpczsbutwtctoawqdpxsmvickirmwwookmemnaysbjmipnylmgpizdxtgnlvoacisjzryoesutacybmhzwhdmkwjqmpjbpeskfsmkqwtmcmswddjccxlnbncbgsmcwmuzfhplmmcfjpabfujnhcogvwmlvzqpcteckrghzogfvsixstbxwssbxzauiqvudqoqrltinafbfhlfzrtvgtngufkvwplcgfmwqpxhgwsfobehfvnlixeslzmbqdcrsxgoekxldtzsctjdvfqfzbtieaeexnksxarchfptdasywndwvlsteflwqaymysihzlpldqcocpblommkahgsxjbapdavcgakhvvfjrutypaccamiehhqfopjxcubuvkqujowyjtxahsrvsdchqvhwlvnassmedwharsnqbrrsbhemhbmenmckargekuyrsirxbvwuuoetiwovzodglgiyafzsqvvnqdhmxdmqpiyikpdifojctjzfeizpwzxkoianrkzamihycdhqfyypfkdtmxzoakifnrwbndlnfaootgdxembvduizsorlcebledprispmxzhtvwropbcitvlpzmpzkjnuxabwfedwxcigjsmgsmrrawxuqttlksmtdymptphmztkv"

print(Solution().solve(A))