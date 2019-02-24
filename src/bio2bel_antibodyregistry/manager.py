# -*- coding: utf-8 -*-

"""Manager for Bio2BEL Antibody Registry."""

from typing import Mapping, Optional

from bio2bel import AbstractManager
from bio2bel.manager.flask_manager import FlaskMixin
from bio2bel.manager.namespace_manager import BELNamespaceManagerMixin
from pybel.manager.models import Namespace, NamespaceEntry
from tqdm import tqdm

from .constants import MODULE_NAME
from .models import Antibody, Base
from .parser import df_getter

__all__ = [
    'Manager',
]


class Manager(AbstractManager, BELNamespaceManagerMixin, FlaskMixin):
    """Manages the Bio2BEL Antibody Registry database."""

    module_name = MODULE_NAME
    namespace_model = Antibody
    flask_admin_models = [Antibody]
    _base = Base

    def is_populated(self) -> bool:
        """Check if the Bio2BEL Antibody Registry database is populated."""
        return 0 < self.count_antibodies()

    def count_antibodies(self) -> int:
        """Count the number of antibodies in the database."""
        return self._count_model(Antibody)

    def summarize(self) -> Mapping[str, int]:
        """Summarize the contents of the Bio2BEL Antibody Registry database."""
        return dict(antibodies=self.count_antibodies())

    def populate(self, url: Optional[str] = None) -> None:
        """Populate the Bio2BEL Antibody Registry database."""
        chunks = df_getter(url=url)
        for df in tqdm(chunks):
            df = df[df.name.notna()]
            df = df[df.antibodyregistry_id.notna()]
            df = df[df.vendor.notna()]
            df.to_sql(Antibody.__tablename__, con=self.engine, if_exists='append', index=False)
            self.session.commit()

    def get_antibody_by_antibodyregistry_id(self, antibodyregistry_id: str) -> Optional[Antibody]:
        """Get an antibody by its registry identifier, if it exists."""
        return self.session.query(Antibody).filter(Antibody.antibodyregistry_id == antibodyregistry_id).one_or_none()

    def _create_namespace_entry_from_model(self, model: Antibody, namespace: Namespace) -> NamespaceEntry:
        return NamespaceEntry(
            namespace=namespace,
            identifier=model.antibodyregistry_id,
            name=model.name,
            encoding='A',
        )
