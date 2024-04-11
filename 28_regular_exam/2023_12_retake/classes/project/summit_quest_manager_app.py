from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    VALID_CLIMBER_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAK_TYPES = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):

        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        climber = next(filter(lambda c: c.name == climber_name, self.climbers), None)
        if climber:
            return f"{climber_name} has been already registered."

        self.climbers.append(self.VALID_CLIMBER_TYPES[climber_type](climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(self.VALID_PEAK_TYPES[peak_type](peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):

        climber = next(filter(lambda c: c.name == climber_name, self.climbers), None)
        peak = next(filter(lambda p: p.name == peak_name, self.peaks), None)
        missing_gear = []
        recommended_gear = peak.get_recommended_gear()
        for needed_gear in recommended_gear:
            if needed_gear not in gear:
                climber.is_prepared = False
                missing_gear.append(needed_gear)
        missing_gear.sort()
        if not climber.is_prepared:
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(missing_gear)}."
        return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = next(filter(lambda c: c.name == climber_name, self.climbers), None)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = next(filter(lambda p: p.name == peak_name, self.peaks), None)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        able_to_climb = climber.can_climb()
        is_prepared_to_climb = climber.is_prepared

        if able_to_climb and is_prepared_to_climb:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        if not is_prepared_to_climb:
            return f"{climber_name} will need to be better prepared next time."

        if not able_to_climb:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        result = ""
        all_conquered_peaks = []
        all_climbers = sorted(
            filter(lambda c: c.conquered_peaks, self.climbers), key=lambda c: (-len(c.conquered_peaks), c.name)
        )

        winning_climbers = []
        for climber in all_climbers:
            if len(climber.conquered_peaks) > 0:
                for peak in climber.conquered_peaks:
                    if peak not in all_conquered_peaks:
                        all_conquered_peaks.append(peak)

                climber.conquered_peaks = sorted(climber.conquered_peaks)

                winning_climbers.append(climber)

        result += f"Total climbed peaks: {len(all_conquered_peaks)}\n"
        result += f"**Climber's statistics:**\n"
        for climber in winning_climbers:
            string_climber = str(climber)
            result += f"{string_climber}\n"

        return result.strip()
