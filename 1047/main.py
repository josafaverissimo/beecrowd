class Game():
    def __init__(
        self,
        start_hour,
        start_minute,
        end_hour,
        end_minute
    ):
        self.__start_hour = int(start_hour)
        self.__start_minute = int(start_minute)
        self.__end_hour = int(end_hour)
        self.__end_minute = int(end_minute)

    def calculate_duration(self):
        def calculate_hour_duration(start_hour, end_hour, is_lower_than_a_minute):
            duration = end_hour - start_hour
            duration += 24 if duration <= 0 else 0
            duration -= 1 if is_lower_than_a_minute else 0

            return duration

        def calculate_minute_duration(start_minute, end_minute):
            duration = end_minute - start_minute
            duration += 60 if duration < 0 else 0

            return duration

        minute_duration = calculate_minute_duration(self.__start_minute, self.__end_minute)
        hour_duration = calculate_hour_duration(self.__start_hour, self.__end_hour, self.__start_minute > self.__end_minute)

        return {
            'minute_duration': minute_duration,
            'hour_duration': hour_duration
        }

    def __str__(self):
        duration = self.calculate_duration()

        return f'O JOGO DUROU {duration["hour_duration"]} HORA(S) E {duration["minute_duration"]} MINUTO(S)'


game_times = input().split(' ')
start_hour = game_times[0]
start_minute = game_times[1]
end_hour = game_times[2]
end_minute = game_times[3]

death_game = Game(start_hour, start_minute, end_hour, end_minute)

print(death_game)