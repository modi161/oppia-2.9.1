# Copyright 2020 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Check for decrease in coverage from 100% of frontend files."""

from __future__ import absolute_import  # pylint: disable=import-only-modules
from __future__ import unicode_literals  # pylint: disable=import-only-modules

import os
import re
import sys

import python_utils

LCOV_FILE_PATH = os.path.join(os.pardir, 'karma_coverage_reports', 'lcov.info')
RELEVANT_LCOV_LINE_PREFIXES = ['SF', 'LH', 'LF']

# Contains the name of all files that reached up to 100% of coverage.
# This list must be kept up-to-date; the changes should be done manually.
# Please keep the list in alphabetical order.
# NOTE TO REVIEWERS: Please be circumspect about any PRs which delete elements
# from this list.
FULLY_COVERED_FILENAMES = [
    'about-page.controller.ts',
    'admin-config-tab-backend-api.service.ts',
    'admin-data.service.ts',
    'admin-page.constants.ajs.ts',
    'admin-page.constants.ts',
    'admin-router.service.ts',
    'admin-task-manager.service.ts',
    'alerts.service.ts',
    'angular-name.service.ts',
    'answer-groups-cache.service.ts',
    'AnswerClassificationResultObjectFactory.ts',
    'AnswerDetailsImprovementTaskObjectFactory.ts',
    'AnswerGroupObjectFactory.ts',
    'AnswerStatsObjectFactory.ts',
    'app.constants.ajs.ts',
    'app.constants.ts',
    'apply-validation.directive.ts',
    'assets-backend-api.service.ts',
    'audio-translation-language.service.ts',
    'AudioFileObjectFactory.ts',
    'AudioLanguageObjectFactory.ts',
    'AutogeneratedAudioLanguageObjectFactory.ts',
    'autoplayed-videos.service.ts',
    'background-mask.service.ts',
    'base-undo-redo.service.ts',
    'browser-checker.service.ts',
    'camel-case-to-hyphens.filter.ts',
    'camel-case-to-hyphens.pipe.ts',
    'capitalize.filter.ts',
    'capitalize.pipe.ts',
    'ChangeObjectFactory.ts',
    'ClassifierObjectFactory.ts',
    'classifiers-extension.constants.ts',
    'classroom-domain.constants.ajs.ts',
    'classroom-domain.constants.ts',
    'code-normalizer.service.ts',
    'code-repl-rules.service.ts',
    'code-repl-validation.service.ts',
    'codemirrorRequires.ts',
    'CodeRepl.ts',
    'collection-creation-backend-api.service.ts',
    'collection-domain.constants.ajs.ts',
    'collection-domain.constants.ts',
    'collection-editor-page.constants.ajs.ts',
    'collection-editor-page.constants.ts',
    'collection-linearizer.service.ts',
    'collection-rights-backend-api.service.ts',
    'collection-summary-tile.constants.ajs.ts',
    'collection-summary-tile.constants.ts',
    'collection-validation.service.ts',
    'CollectionRightsObjectFactory.ts',
    'community-dashboard-page.constants.ajs.ts',
    'community-dashboard-page.constants.ts',
    'compare-versions.service.ts',
    'compute-graph.service.ts',
    'concept-card-backend-api.service.ts',
    'constants.ts',
    'construct-translation-ids.service.ts',
    'continue-rules.service.ts',
    'continue-validation.service.ts',
    'Continue.ts',
    'convert-html-to-unicode.filter.ts',
    'convert-unicode-to-html.filter.ts',
    'convert-unicode-with-params-to-html.filter.ts',
    'count-vectorizer.service.ts',
    'creator-dashboard-backend-api.service.ts',
    'creator-dashboard-page.constants.ajs.ts',
    'creator-dashboard-page.constants.ts',
    'data.ts',
    'date-time-format.service.ts',
    'debug-info-tracker.service.ts',
    'device-info.service.ts',
    'document-attribute-customization.service.ts',
    'drag-and-drop-sort-input-rules.service.ts',
    'DragAndDropSortInput.ts',
    'editability.service.ts',
    'editable-question-backend-api.service.ts',
    'editable-skill-backend-api.service.ts',
    'editable-topic-backend-api.service.ts',
    'editor-domain.constants.ajs.ts',
    'editor-domain.constants.ts',
    'editor-first-time-events.service.ts',
    'email-dashboard-page.controller.ts',
    'end-exploration-rules.service.ts',
    'end-exploration-validation.service.ts',
    'EndExploration.ts',
    'EntityContextObjectFactory.ts',
    'exploration-correctness-feedback.service.ts',
    'exploration-data.service.ts',
    'exploration-editor-page.constants.ajs.ts',
    'exploration-editor-page.constants.ts',
    'exploration-features-backend-api.service.ts',
    'exploration-html-formatter.service.ts',
    'exploration-init-state-name.service.ts',
    'exploration-param-changes.service.ts',
    'exploration-player-page.constants.ajs.ts',
    'exploration-player-page.constants.ts',
    'exploration-property.service.ts',
    'exploration-rights.service.ts',
    'exploration-summary-backend-api.service.ts',
    'exploration-title.service.ts',
    'ExplorationDraftObjectFactory.ts',
    'ExplorationObjectFactory.ts',
    'ExplorationOpportunitySummaryObjectFactory.ts',
    'expression-parser.service.ts',
    'extension-tag-assembler.service.ts',
    'extract-image-filenames-from-state.service.ts',
    'FeedbackImprovementTaskObjectFactory.ts',
    'FeedbackMessageSummaryObjectFactory.ts',
    'FeedbackThreadObjectFactory.ts',
    'FileDownloadRequestObjectFactory.ts',
    'focus-manager.service.ts',
    'format-rte-preview.filter.ts',
    'fraction-input-rules.service.ts',
    'FractionInput.ts',
    'FractionObjectFactory.ts',
    'generate-content-id.service.ts',
    'generatedDefaultData.ts',
    'get-abbreviated-text.filter.ts',
    'get-abbreviated-text.pipe.ts',
    'graph-data.service.ts',
    'graph-utils.service.ts',
    'GraphInput.ts',
    'guest-collection-progress.service.ts',
    'GuestCollectionProgressObjectFactory.ts',
    'HintObjectFactory.ts',
    'hints-and-solution-manager.service.ts',
    'id-generation.service.ts',
    'image-click-input-rules.service.ts',
    'image-click-input-validation.service.ts',
    'image-preloader.service.ts',
    'ImageClickInput.ts',
    'ImageFileObjectFactory.ts',
    'ImprovementActionButtonObjectFactory.ts',
    'improvements-display.service.ts',
    'improvements.service.ts',
    'interaction-details-cache.service.ts',
    'interaction-specs.constants.ajs.ts',
    'interaction-specs.constants.ts',
    'InteractionObjectFactory.ts',
    'interactions-extension.constants.ajs.ts',
    'interactions-extension.constants.ts',
    'interactionsQuestionsRequires.ts',
    'interactionsRequires.ts',
    'interactive-map-rules.service.ts',
    'interactive-map-validation.service.ts',
    'InteractiveMap.ts',
    'is-at-least.filter.ts',
    'is-at-most.filter.ts',
    'is-float.filter.ts',
    'is-integer.filter.ts',
    'is-nonempty.filter.ts',
    'item-selection-input-rules.service.ts',
    'ItemSelectionInput.ts',
    'learner-action-render.service.ts',
    'learner-answer-details-data.service.ts',
    'learner-dashboard-backend-api.service.ts',
    'learner-dashboard-ids-backend-api.service.ts',
    'learner-dashboard-page.constants.ajs.ts',
    'learner-dashboard-page.constants.ts',
    'learner-params.service.ts',
    'learner-playlist-modal.controller.ts',
    'learner-playlist.service.ts',
    'LearnerActionObjectFactory.ts',
    'LearnerAnswerDetailsObjectFactory.ts',
    'LearnerAnswerInfoObjectFactory.ts',
    'LearnerDashboardActivityIdsObjectFactory.ts',
    'library-page.constants.ajs.ts',
    'library-page.constants.ts',
    'local-storage.service.ts',
    'logger.service.ts',
    'logic-proof-rules.service.ts',
    'logic-proof-validation.service.ts',
    'LogicProof.ts',
    'mark-all-audio-and-translations-as-needing-update.controller.ts',
    'MathExpressionInput.ts',
    'mathjaxConfig.ts',
    'meta-tag-customization.service.ts',
    'MisconceptionObjectFactory.ts',
    'multiple-choice-input-rules.service.ts',
    'multiple-choice-input-validation.service.ts',
    'MultipleChoiceInput.ts',
    'music-notes-input-validation.service.ts',
    'MusicNotesInput.ts',
    'navigation.service.ts',
    'nested-directives-recursion-timeout-prevention.service.ts',
    'normalize-whitespace.filter.ts',
    'normalize-whitespace.pipe.ts',
    'notifications-dashboard-page.controller.ts',
    'number-attempts.service.ts',
    'number-with-units-rules.service.ts',
    'NumberWithUnits.ts',
    'numeric-input-rules.service.ts',
    'NumericInput.ts',
    'objectComponentsRequires.ts',
    'objectComponentsRequiresForPlayers.ts',
    'objects-domain.constants.ajs.ts',
    'objects-domain.constants.ts',
    'OutcomeObjectFactory.ts',
    'page-title.service.ts',
    'ParamChangeObjectFactory.ts',
    'ParamChangesObjectFactory.ts',
    'ParamMetadataObjectFactory.ts',
    'ParamSpecObjectFactory.ts',
    'ParamSpecsObjectFactory.ts',
    'ParamTypeObjectFactory.ts',
    'pencil-code-editor-rules.service.ts',
    'PencilCodeEditor.ts',
    'playthrough-issues-backend-api.service.ts',
    'PlaythroughImprovementTaskObjectFactory.ts',
    'PlaythroughIssueObjectFactory.ts',
    'PlaythroughObjectFactory.ts',
    'practice-session-page.constants.ajs.ts',
    'practice-session-page.constants.ts',
    'PredictionResultObjectFactory.ts',
    'question-domain.constants.ajs.ts',
    'question-domain.constants.ts',
    'question-player-state.service.ts',
    'question-player.constants.ajs.ts',
    'question-player.constants.ts',
    'question-undo-redo.service.ts',
    'questions-list.constants.ajs.ts',
    'questions-list.constants.ts',
    'questions-list.service.ts',
    'QuestionSummaryForOneSkillObjectFactory.ts',
    'QuestionSummaryObjectFactory.ts',
    'read-only-exploration-backend-api.service.ts',
    'ReadOnlyStoryNodeObjectFactory.ts',
    'ReadOnlySubtopicPageObjectFactory.ts',
    'replace-inputs-with-ellipses.filter.ts',
    'replace-inputs-with-ellipses.pipe.ts',
    'require-is-float.directive.ts',
    'review-test-backend-api.service.ts',
    'review-test-domain.constants.ts',
    'review-test-engine.service.ts',
    'review-test-page.constants.ajs.ts',
    'review-test-page.constants.ts',
    'rich_text_components_definitions.ts',
    'richTextComponentsRequires.ts',
    'rte-helper-modal.controller.ts',
    'rte-helper.service.ts',
    'RubricObjectFactory.ts',
    'RuleObjectFactory.ts',
    'schema-default-value.service.ts',
    'schema-undefined-last-element.service.ts',
    'search-explorations-backend-api.service.ts',
    'search.service.ts',
    'services.constants.ajs.ts',
    'services.constants.ts',
    'set-input-rules.service.ts',
    'set-input-validation.service.ts',
    'SetInput.ts',
    'sidebar-status.service.ts',
    'site-analytics.service.ts',
    'skill-domain.constants.ajs.ts',
    'skill-domain.constants.ts',
    'skill-editor-page.constants.ajs.ts',
    'skill-editor-page.constants.ts',
    'skill-editor-routing.service.ts',
    'skill-mastery-backend-api.service.ts',
    'skill-rights-backend-api.service.ts',
    'SkillOpportunityObjectFactory.ts',
    'SkillRightsObjectFactory.ts',
    'skills-mastery-list.constants.ajs.ts',
    'skills-mastery-list.constants.ts',
    'SkillSummaryObjectFactory.ts',
    'solution-validity.service.ts',
    'solution-verification.service.ts',
    'SolutionObjectFactory.ts',
    'splash-page.controller.ts',
    'state-classifier-mapping.service.ts',
    'state-content.service.ts',
    'state-customization-args.service.ts',
    'state-editor.constants.ajs.ts',
    'state-editor.constants.ts',
    'state-interaction-id.service.ts',
    'state-recorded-voiceovers.service.ts',
    'state-rules-stats.service.ts',
    'state-solicit-answer-details.service.ts',
    'state-solution.service.ts',
    'state-top-answers-stats-backend-api.service.ts',
    'state-written-translations.service.ts',
    'StateObjectFactory.ts',
    'statistics-domain.constants.ajs.ts',
    'statistics-domain.constants.ts',
    'StopwatchObjectFactory.ts',
    'story-domain.constants.ajs.ts',
    'story-domain.constants.ts',
    'story-editor-page.constants.ajs.ts',
    'story-editor-page.constants.ts',
    'story-viewer-domain.constants.ts',
    'StoryObjectFactory.ts',
    'StoryPlaythroughObjectFactory.ts',
    'StoryReferenceObjectFactory.ts',
    'StorySummaryObjectFactory.ts',
    'SubtitledHtmlObjectFactory.ts',
    'subtopic-viewer-backend-api.service.ts',
    'subtopic-viewer-domain.constants.ts',
    'SubtopicPageContentsObjectFactory.ts',
    'suggestion-modal.service.ts',
    'SuggestionImprovementTaskObjectFactory.ts',
    'SuggestionObjectFactory.ts',
    'SuggestionThreadObjectFactory.ts',
    'summarize-nonnegative-number.filter.ts',
    'teach-page.controller.ts',
    'test.extras.ts',
    'text-input-prediction.service.ts',
    'text-input-rules.service.ts',
    'text-input-validation.service.ts',
    'text-input.tokenizer.ts',
    'TextInput.ts',
    'thread-data.service.ts',
    'thread-status-display.service.ts',
    'topic-domain.constants.ajs.ts',
    'topic-domain.constants.ts',
    'topic-editor-page.constants.ajs.ts',
    'topic-editor-page.constants.ts',
    'topic-landing-page.constants.ajs.ts',
    'topic-landing-page.constants.ts',
    'topic-rights-backend-api.service.ts',
    'topic-viewer-domain.constants.ajs.ts',
    'topic-viewer-domain.constants.ts',
    'TopicRightsObjectFactory.ts',
    'topics-and-skills-dashboard-domain.constants.ajs.ts',
    'topics-and-skills-dashboard-domain.constants.ts',
    'topics-and-skills-dashboard-page.constants.ajs.ts',
    'topics-and-skills-dashboard-page.constants.ts',
    'TopicSummaryObjectFactory.ts',
    'translation-language.service.ts',
    'translation-status.service.ts',
    'translation-tab-active-content-id.service.ts',
    'translation-tab-active-mode.service.ts',
    'truncate-at-first-ellipsis.filter.ts',
    'truncate-at-first-ellipsis.pipe.ts',
    'truncate-at-first-line.filter.ts',
    'truncate-at-first-line.pipe.ts',
    'uiLeafletRequires.ts',
    'underscores-to-camel-case.filter.ts',
    'underscores-to-camel-case.pipe.ts',
    'undo-redo.service.ts',
    'UpgradedServices.ts',
    'url.service.ts',
    'user-email-preferences.service.ts',
    'user-exploration-permissions.service.ts',
    'user.service.ts',
    'UserInfoObjectFactory.ts',
    'validators.service.ts',
    'valueGeneratorsRequires.ts',
    'VoiceoverObjectFactory.ts',
    'window-dimensions.service.ts',
    'window-ref.service.ts',
    'winnowing-preprocessing.service.ts',
    'wrap-text-with-ellipsis.filter.ts',
    'wrap-text-with-ellipsis.pipe.ts',
    'WrittenTranslationObjectFactory.ts',
    'WrittenTranslationsObjectFactory.ts',
]


class LcovStanzaRelevantLines(python_utils.OBJECT):
    """Gets the relevant lines from a lcov stanza."""

    def __init__(self, stanza):
        """Initialize the object which provides relevant data of a lcov
        stanza in order to calculate any decrease in frontend test coverage.

        Args:
            stanza: list(str). Contains all the lines from a lcov stanza.

        Raises:
            Exception: file_path is empty.
            Exception: Total lines number is not found.
            Exception: Covered lines number is not found.
        """

        match = re.search('SF:(.+)\n', stanza)
        if match is None:
            raise Exception(
                'The test path is empty or null. '
                'It\'s not possible to diff the test coverage correctly.')
        _, file_name = os.path.split(match.group(1))
        self.file_name = file_name

        match = re.search(r'LF:(\d+)\n', stanza)
        if match is None:
            raise Exception(
                'It wasn\'t possible to get the total lines of {} file.'
                'It\'s not possible to diff the test coverage correctly.'
                .format(file_name))
        self.total_lines = int(match.group(1))

        match = re.search(r'LH:(\d+)\n', stanza)
        if match is None:
            raise Exception(
                'It wasn\'t possible to get the covered lines of {} file.'
                'It\'s not possible to diff the test coverage correctly.'
                .format(file_name))
        self.covered_lines = int(match.group(1))


def get_stanzas_from_lcov_file():
    """Get all stanzas from a lcov file. The lcov file gather all the frontend
    files that has tests and each one has the following structure:
    TN: test name
    SF: file path
    FNF: total functions
    FNH: functions covered
    LF: total lines
    LH: lines covered
    BRF: total branches
    BRH: branches covered
    end_of_record

    Returns:
        list(LcovStanzaRelevantLines). A list with all stanzas.
    """
    f = python_utils.open_file(LCOV_FILE_PATH, 'r')
    lcov_items_list = f.read().split('end_of_record')
    stanzas_list = []

    for item in lcov_items_list:
        if item.strip('\n'):
            stanza = LcovStanzaRelevantLines(item)
            stanzas_list.append(stanza)

    return stanzas_list


def check_fully_covered_filenames_list_is_sorted():
    """Check if FULLY_COVERED_FILENAMES list is in alphabetical order."""
    if FULLY_COVERED_FILENAMES != sorted(
            FULLY_COVERED_FILENAMES, key=lambda s: s.lower()):
        sys.exit('The \033[1mFULLY_COVERED_FILENAMES\033[0m list must be kept'
                 ' in alphabetical order.')


def check_coverage_changes():
    """Checks if the whitelist for fully covered files needs to be changed by:
    - New file insertion
    - File renaming
    - File deletion

    Raises:
        Exception: LCOV_FILE_PATH doesn't exist.
    """
    if not os.path.exists(LCOV_FILE_PATH):
        raise Exception('Expected lcov file to be available at {}, but the'
                        ' file does not exist.'.format(LCOV_FILE_PATH))

    stanzas = get_stanzas_from_lcov_file()
    whitelist = list(FULLY_COVERED_FILENAMES)
    errors = ''

    for stanza in stanzas:
        file_name = stanza.file_name
        total_lines = stanza.total_lines
        covered_lines = stanza.covered_lines

        if file_name in whitelist:
            if total_lines != covered_lines:
                errors += ('\033[1m{}\033[0m file is in the whitelist but its'
                           ' coverage decreased. Make sure it is fully covered'
                           ' by Karma unit tests.\n'.format(file_name))

            whitelist.remove(file_name)
        else:
            if total_lines == covered_lines:
                errors += ('\033[1m{}\033[0m file is fully covered but it\'s'
                           ' not in the "100% coverage" whitelist. Please add'
                           ' the file name in the whitelist in the file'
                           ' scripts/check_frontend_test_coverage.py.\n'
                           .format(file_name))

    if whitelist:
        for test_name in whitelist:
            errors += ('\033[1m{}\033[0m is in the frontend test coverage'
                       ' whitelist but it doesn\'t exist anymore. If you have'
                       ' renamed it, please make sure to remove the old file'
                       ' name and add the new file name in the whitelist in'
                       ' the file scripts/check_frontend_test_coverage.py.\n'
                       .format(test_name))

    if errors:
        python_utils.PRINT('------------------------------------')
        python_utils.PRINT('Frontend Coverage Checks Not Passed.')
        python_utils.PRINT('------------------------------------')
        sys.exit(errors)
    else:
        python_utils.PRINT('------------------------------------')
        python_utils.PRINT('All Frontend Coverage Checks Passed.')
        python_utils.PRINT('------------------------------------')

    check_fully_covered_filenames_list_is_sorted()


def main():
    """Runs all the steps for checking if there is any decrease of 100% covered
    files in the frontend.
    """
    check_coverage_changes()


# The 'no coverage' pragma is used as this line is un-testable. This is because
# it will only be called when wrap_up_release.py is used as a script.
if __name__ == '__main__': # pragma: no cover
    main()
