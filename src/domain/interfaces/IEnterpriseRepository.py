from src.domain.entities.enterprise import Enterprise


class IEnterpriseRepository:
    def get_by_id(self, enterprise_id: str):
        raise NotImplementedError

    def add(self, enterprise: Enterprise):
        raise NotImplementedError

    def update(self, enterprise: Enterprise):
        raise NotImplementedError

    def delete(self, enterprise_id: str):
        raise NotImplementedError