"""
Features package for the microlearning application.
Contains modular features like sidebar, navigation, etc.
"""

from .sidebar import configure_sidebar, render_progress_indicator, render_section_navigation, render_current_section_info

__all__ = ['configure_sidebar', 'render_progress_indicator', 'render_section_navigation', 'render_current_section_info']
