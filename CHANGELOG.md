# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.3.0] - 2020-12-16

### Added
- Add `CoverageArea` model and coverage area foreign key relations in `TrafficSignReal` and `AdditionalSignReal`
- Add a management command to import parking areas as coverage areas from Helsinki City WFS
- Update `Plan` model `plan_number` help_text and change `decision_maker` from ForeignKey to CharField
- Assign `device_type` based on `legacy_code` to `AdditionalSignContentReal` and `AdditionalSignContentPlan` instances
- Add `source_name` and `source_id` to `AdditionalSignContentReal` and `AdditionalSignContentPlan` and update importers accordingly
- Improve fields naming in Plan API endpoint to make it more understandable
- Remove `decision_date` and `decision_id` from traffic control plan models
- Improve admin map view feature info window to include more fields
- Set `Plan` `linked_objects` as read-only
- Improve feature info window to include more details and add localization to it
- Add CoverageAreaCategory and CoverageArea to django admin
- Use icon select widget for AdditionalSignContentPlan/Real inlines
- Convert all 2d geometry fields to 3d
- Add traffic control operation models and include operations in admin and REST API
- Add direction indicator to traffic signs
- Add management command to generate traffic sign plan icons
- Add icon, value, unit and size fields to TrafficControlDeviceType model
- Use device type value for traffic sign and signpost value field if not provided
- Add API-root and API-documentation links to Admin UI front page

### Changed
- Change TrafficSign and Signpost value field from IntegerField to DecimalField
- Extract numeric values from text column when importing blom kartta traffic signs
- Force 3d geometries when importing coverage areas and operational areas from HKI WFS

### Fixed
- Fix the styling of traffic sign icon widget so that the icon and select are in the same row

## [1.2.0] - 2020-09-29

### Added
- Add `source_name` and `source_id` to all TrafficControl models
- `Owner` model and foreign key relation to it for all TrafficControl models
- Add management command to import operational areas (contract areas) from Helsinki WFS
- Show traffic sign icon next to `device_type` in `TrafficSignPlan` and `TrafficSignReal` admin
- Add traffic control device types filtering by target model

### Changed
- Open attachments in new tab in admin
- The `content` attribute of `AdditionalSignPlan` and `AdditionalSignReal` models are no longer
  read only in the API.
- Move general information to be the first fieldset in admin views

### Fixed
- Traffic control model admin performance issues caused by multiple foreign key choices

## [1.1.0] - 2020-09-01

### Added
- Permissions based on operational area
- `traffic_sign_type` property for `TrafficControlDeviceType`
- Added tests for Katajanokka importer
- Add traffic sign type list filter to `TrafficControlDeviceTypeAdmin`
- Allow users to authenticate to the REST API with Token
- Add a layer model and a map view to visualize data on the map
- Add REST API endpoint for `OperationalArea`
- Show admin links when clicking features on map view
- Turn map view into a React app with Material UI

### Changed
- Admin UI usability improvements
- Add `description_fi` field for `MountType`
- Improved the plan geometry generation
- Application root URL is changed to `/city-infra`
- Remove `color` attribute from `TrafficSignPlan` and `TrafficSignReal`

### Fixed
- Fixed a bug that creating `TrafficControlDeviceType` crashes when target model is specified

## [1.0.0] - 2020-07-07

First release of the City Infrastructure Platform API.

Provides an API for handling and storing common Traffic Control entities, such as TrafficSigns and RoadMarkings.

### Added
- Traffic Control REST API
- Traffic Control models:
  - `TrafficSignPlan` and `TrafficSignReal`
  - `AdditionalSignPlan` and `AdditionalSignReal`
  - `TrafficLightPlan` and `TrafficLightReal`
  - `RoadMarkingPlan` and `RoadMarkingReal`
  - `SignpostPlan` and `SignpostReal`
  - `BarrierPlan` and `BarrierReal`
  - `MountPlan` and `MountReal`
  - `Plan`
- SSO-login with TokenAuthentication

[unreleased]: https://github.com/City-of-Helsinki/city-infrastructure-platform/compare/v1.3.0...HEAD
[1.3.0]: https://github.com/City-of-Helsinki/city-infrastructure-platform/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/City-of-Helsinki/city-infrastructure-platform/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/City-of-Helsinki/city-infrastructure-platform/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/City-of-Helsinki/city-infrastructure-platform/compare/v0.0.1...v1.0.0
