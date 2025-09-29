# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

# to find if the you'd make it to all stations
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        diff = []
        for idx in range(len(gas)):
            diff.append(gas[idx] - cost[idx])
        return sum(diff) >= 0
    

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_gas = 0
        total_cost = 0
        start_index = 0
        tank = 0

        for idx in range(len(gas)):
            total_gas += gas[idx]
            total_cost += cost[idx]
            tank += gas[idx] - cost[idx]

            if tank < 0:
                start_index = idx+ 1
                tank = 0

        if total_gas < total_cost:
            return -1
        
        return start_index


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
solution = Solution()
print(solution.canCompleteCircuit(gas, cost))