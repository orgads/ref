{
  'targets': [
    {
      'target_name': 'ref',
      'sources': [ 'src/binding.cc' ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")'
      ],
    },
    {
      'target_name': 'action_after_build',
      'type': 'none',
      'dependencies': ['ref'],
      'copies': [{
        'files': ['<(PRODUCT_DIR)/ref.node'],
        'destination': 'out',
      }],
    },
  ]
}
