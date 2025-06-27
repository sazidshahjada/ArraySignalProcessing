class CATARCSModel:
    def __init__(self, M, N, d=0.5):
        self.M = M
        self.N = N
        self.d = d  # Inter-element spacing, default is λ/2, but used as 1 for integer positions
        self.F = 2  # Compression factor
        self.M_prime = self.M // self.F  # Since M = F * M'
        self.L = self.M + self.N  # Translocation value
        self.number_of_sensors = 2 * self.M + self.N - 1

    def sensor_positions(self):
        # Subarray 1: N sensors, starting at 0
        S1 = [i * self.M_prime * self.d for i in range(0, self.N)]
    
        # Subarray 2: 2M-1 sensors, translocated by L
        S2 = [(i * self.N + self.L) * self.d
              for i in range(0, 2 * self.M - 1)]
        
        # Combine and sort sensor positions
        S = list(set(S1 + S2))  # Use set to ensure no duplicates
        S.sort()  # Sort in ascending order
        
        return S