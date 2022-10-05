from gtclab.models.normalgame import NormalGame

if __name__ == "__main__":
    normal = NormalGame(
        num_players=2, 
        num_choices= {1: 2, 2: 2},
        utility_matrices= {1: [[1,2],
                            [2,1]],
                        2: [[1,2],
                            [2,1]]}
        )
    print(normal)