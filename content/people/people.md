---
# An instance of the People widget.
# Documentation: https://wowchemy.com/docs/page-builder/
widget: members

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 68

title: Meet the Team
subtitle:

content:
  # Choose which groups/teams of users to display.
  #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
  user_groups:
    - Principal Investigators
    - PhD Students
    - Masters Students
    - Undergraduate Students
    - Alumni
  page_type: authors
  # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
  filter_default: 0

  # Filter toolbar (optional).
  # Add or remove as many filters (`filter_button` instances) as you like.
  # To show all items, set `tag` to "*".
  # To filter by a specific tag, set `tag` to an existing tag name.
  # To remove the toolbar, delete the entire `filter_button` block.
  filter_button:
    - name: All
      tag: '*'


design:
  show_interests: false
  show_role: true
  show_social: true
  show_bio: false
  show_organizations: true
  view: 'profile_card'
  columns: '1'

---
