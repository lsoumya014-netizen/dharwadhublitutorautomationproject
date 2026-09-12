"""Page object exports for DharwadHubballiTutor test suite."""

from .about import aboutPage
from .catalogue import CataloguePage
from .contact import contactPage
from .demo import Demopage
from .home import HomePage
from .LMS import LMSPage
from .placement import placementPage

__all__ = [
    "HomePage",
    "contactPage",
    "Demopage",
    "aboutPage",
    "placementPage",
    "LMSPage",
    "CataloguePage",
]
