from abc import ABC, abstractmethod
from datetime import timedelta

class Job(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass


    @property
    @abstractmethod
    def delay(self) -> timedelta:
        pass

    @abstractmethod
    async def run(self):
        pass

_jobs: list[Job] = []

def get_all_jobs():
    from worker.jobs import log_processor, role_checker, discord_refresh, unban_players_checker, ip_check, expired_token_check
    if not _jobs:
        _jobs.extend(log_processor.get_jobs())
        _jobs.extend(role_checker.get_jobs())
        _jobs.extend(discord_refresh.get_jobs())
        _jobs.extend(unban_players_checker.get_jobs())
        _jobs.extend(ip_check.get_jobs())
        _jobs.extend(expired_token_check.get_jobs())
    return _jobs